from Telas.tela_luta import TelaLuta
from random import randint
from enum import Enum


class FightNumbers(Enum):
    ROUND = 3
    STAMINA = 4
    SEMI_FINAL = 4
    QUARTAS_DE_FINAL = 8
    MYKE_TYSON = 1
    TONY_TUCKER = 3
    MULTIPLICADOR_LUTADORES = 2


class ControladorLuta:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_luta = TelaLuta()
        self.__lutas = []
        self.__start_game = False
        self.__quantidade_lutadores = 0
        self.__boxeador_usuario = None
        self.__vitoria_boxeador_usuario = False
        self.__jogadas_usuario = []

    @property
    def lista_lutas(self):
        return self.__lutas

    @property
    def boxeador_usuario(self):
        return self.__boxeador_usuario

    @property
    def vitoria_boxeador_usuario(self):
        return self.__vitoria_boxeador_usuario

    @property
    def jogadas_usuario(self):
        return self.__jogadas_usuario

    def iniciar_jogo(self):
        fase=None
        if self.__controlador_central.controlador_torneio.torneio_criado:
            lista_lutas = self.__controlador_central.controlador_torneio.lutas
            numero_lutadores = int(self.__controlador_central.controlador_torneio.torneio_atual.numero_lutas * 2)
            if numero_lutadores == FightNumbers.SEMI_FINAL.value:
                fase = 'semi-final'
            elif numero_lutadores == FightNumbers.QUARTAS_DE_FINAL.value:
                fase = 'quartas-de-final'
            for luta in lista_lutas:
                if not luta.boxeador_um.boxeador_cpu:
                    jogador_usuario = luta.boxeador_um
                    jogador_adversario = luta.boxeador_dois
                elif not luta.boxeador_dois.boxeador_cpu:
                    jogador_usuario = luta.boxeador_dois
                    jogador_adversario = luta.boxeador_um
                if not luta.boxeador_um.boxeador_cpu or not luta.boxeador_dois.boxeador_cpu:
                    self.__controlador_central.controlador_torneio.mostrar_luta_usuario(boxeador_um=jogador_usuario, boxeador_dois=jogador_adversario)
                    luta_um, lista_jogadas_usuario, dano_total_causado = self.iniciar_luta(jogador_usuario, jogador_adversario)
                    self.retorna_informacoes_lista(lista_jogadas_usuario, dano_total_causado)
                    if luta_um and fase:
                        self.organizar_campeonato(fase, jogador_usuario, jogador_adversario)
                    else:
                        self.__tela_luta.mostrar_mensagem("-----------------------")
                        self.__tela_luta.mostrar_mensagem("------ GAME OVER ------")
                        self.__tela_luta.mostrar_mensagem("-----------------------")
                        self.__controlador_central.inicializa_sistema()


                else:
                    return self.__tela_luta.mostrar_mensagem("Não iniciará o jogo enquanto não tiver 1 jogador "
                                                             "controlado por você!")
        else:
            self.__tela_luta.mostrar_mensagem("------------------------------ATENÇÃO------------------------------")
            self.__tela_luta.mostrar_mensagem("Não há nenhum torneio cadastrado, é necessário cadastrar o torneio antes")
            self.__tela_luta.mostrar_mensagem("------------------------------------------------------------------")


    def iniciar_luta(self, boxeador_usuario, boxeador_adversario):
        self.__jogadas_usuario = []
        self.__controlador_central.controlador_boxeador.verifica_jogadores_maquina()
        _dano_causado_usuario = 0
        round = 1
        jogada = 0
        game_start = True
        while boxeador_usuario.caracteristica.vida > 0 and boxeador_adversario.caracteristica.vida > 0 and game_start and round <= 4:
            self.__tela_luta.mostrar_mensagem("-------------------")
            self.__tela_luta.mostrar_mensagem(f"Round {round} de {FightNumbers.ROUND.value}")
            self.__tela_luta.mostrar_mensagem("     FIGHT!!")
            self.__tela_luta.mostrar_mensagem("-------------------")
            self.mostrar_luta(boxeador_usuario, boxeador_adversario)
            escolha_inicial = self.__tela_luta.tela_inicio_luta_opcoes()
            if escolha_inicial == 0:
                self.__controlador_central.inicializa_sistema()
            else:
                self.mostrar_luta(boxeador_usuario, boxeador_adversario)
            # Ataque da CPU
            habilidade_escolhida_cpu = self.escolher_habilidade_cpu()
            if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina:
                self.__tela_luta.mostrar_mensagem('-'*50)
                if habilidade_escolhida_cpu.tipo == 'Ataque':
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e te dara {habilidade_escolhida_cpu.dano} de dano")
                elif habilidade_escolhida_cpu.tipo == 'Defesa':
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e bloqueará em {habilidade_escolhida_cpu.taxa_defesa} % o dano")
                elif habilidade_escolhida_cpu.tipo == 'Esquiva':
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e tem {habilidade_escolhida_cpu.taxa_esquiva} % de chance de esquivar do dano")
                self.__tela_luta.mostrar_mensagem('-'*50)
                stamina_cpu_vazia = False
            else:
                self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} não tem stamina suficiente para usar a habilidade {habilidade_escolhida_cpu.tipo}")
                stamina_cpu_vazia = True
            # Ataque do usuário
            # Escolha da habilidade
            lista_id_habilidade = []
            for habilidade in boxeador_usuario.habilidades:
                if habilidade.tipo == 'Ataque':
                    self.__tela_luta.mostrar_habilidade_ataque(habilidade)
                elif habilidade.tipo == 'Defesa':
                    self.__tela_luta.mostrar_habilidade_defesa(habilidade)
                elif habilidade.tipo == 'Esquiva':
                    self.__tela_luta.mostrar_habilidade_esquiva(habilidade)
                lista_id_habilidade.append(int(habilidade.id))
            escolha_habilidade = self.__tela_luta.obtem_id(lista_id_habilidade)
            habilidade_escolhida_usuario = self.busca_por_id(escolha_habilidade, boxeador_usuario.habilidades)
            if boxeador_usuario.caracteristica.stamina <= 0:
                stamina_usuario_vazia = True
            else:
                stamina_usuario_vazia = False
            if habilidade_escolhida_cpu.tipo == 'Ataque' and habilidade_escolhida_usuario.tipo == 'Ataque':
                # Ataque da CPU
                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina and stamina_cpu_vazia == False:
                    dano_causado_ao_usuario = boxeador_usuario.caracteristica.forca + habilidade_escolhida_usuario.dano
                    boxeador_usuario.caracteristica.vida -= dano_causado_ao_usuario
                boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_usuario.custo

                # Ataque do Usuário
                if habilidade_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina and stamina_usuario_vazia == False:
                    dano_causado_a_cpu = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                    boxeador_adversario.caracteristica.vida -= dano_causado_a_cpu
                    _dano_causado_usuario += dano_causado_a_cpu
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo


            elif habilidade_escolhida_cpu.tipo == 'Ataque' and habilidade_escolhida_usuario.tipo == 'Defesa':
                taxa_defesa = 0
                dano_causado_ao_usuario = 0
                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina and stamina_cpu_vazia == False:
                    # Ataque da CPU e defesa do usuário
                    dano_causado_ao_usuario = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

                if habilidade_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina and stamina_usuario_vazia == False:
                    taxa_defesa = habilidade_escolhida_usuario.taxa_defesa / 100
                dano_com_defesa = dano_causado_ao_usuario - (dano_causado_ao_usuario * taxa_defesa)
                boxeador_usuario.caracteristica.vida -= dano_com_defesa
                boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_usuario.custo

            elif habilidade_escolhida_cpu.tipo == 'Ataque' and habilidade_escolhida_usuario.tipo == 'Esquiva':
                # Gerar um número aleatório entre 1 e 100
                numero_aleatorio = randint(1, 100)
                chance_desvio = 0
                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina and stamina_cpu_vazia == False:
                    # Ataque da CPU e esquiva do usuário
                    chance_desvio = habilidade_escolhida_usuario.taxa_esquiva
                boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_usuario.custo

                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina:
                    # Verificar se o número aleatório está dentro da chance de desvio
                    if numero_aleatorio <= chance_desvio:
                        if stamina_usuario_vazia:
                            self.__tela_luta.mostrar_mensagem("WOW que amenteigado que você está! Ataque desviado!")
                    else:
                        dano_cpu = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                        boxeador_usuario.caracteristica.vida -= dano_cpu
                        self.__tela_luta.mostrar_mensagem(f"Hoje não campeão, você não conseguiu desviar do ataque e tomou {dano_cpu} de dano")

                    boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_cpu.custo
                    boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif habilidade_escolhida_usuario.tipo == 'Ataque' and habilidade_escolhida_cpu.tipo == 'Defesa':
                taxa_defesa = 0
                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina and stamina_cpu_vazia == False:
                    taxa_defesa = habilidade_escolhida_cpu.taxa_defesa / 100
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo
                # Ataque do usuário e defesa da CPU
                if habilidade_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina and stamina_usuario_vazia == False:
                    dano_causado_a_cpu = boxeador_usuario.caracteristica.forca + habilidade_escolhida_usuario.dano
                    dano_com_defesa = dano_causado_a_cpu - (dano_causado_a_cpu * taxa_defesa)
                    boxeador_adversario.caracteristica.vida -= dano_com_defesa
                    _dano_causado_usuario += dano_causado_a_cpu
                boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_usuario.custo


            elif habilidade_escolhida_usuario.tipo == 'Ataque' and habilidade_escolhida_cpu.tipo == 'Esquiva':
                # Gerar um número aleatório entre 1 e 100
                numero_aleatorio = randint(1, 100)
                chance_desvio = 0
                if habilidade_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina and stamina_usuario_vazia == False:
                    # Ataque do usuário e esquiva da CPU
                    chance_desvio = habilidade_escolhida_cpu.taxa_esquiva
                    boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_usuario.custo
                # Verificar se o número aleatório está dentro da chance de desvio
                if numero_aleatorio <= chance_desvio:
                    if stamina_cpu_vazia == False:
                        self.__tela_luta.mostrar_mensagem("WOW que amenteigado que você está! Ataque desviado!")
                else:
                    dano_usuario = boxeador_usuario.caracteristica.forca + habilidade_escolhida_usuario.dano
                    boxeador_adversario.caracteristica.vida -= dano_usuario
                    _dano_causado_usuario += dano_usuario
                    self.__tela_luta.mostrar_mensagem(f"Hoje não campeão, você não conseguiu desviar do ataque e tomou {dano_usuario} de dano")
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidade_escolhida_usuario.tipo == 'Defesa'and habilidade_escolhida_cpu.tipo == 'Esquiva'
                    or (habilidade_escolhida_usuario.tipo == 'Esquiva' and habilidade_escolhida_cpu.tipo == 'Defesa')
                    or (habilidade_escolhida_usuario.tipo == 'Defesa' and habilidade_escolhida_cpu.tipo == 'Defesa'))):
                self.__tela_luta.mostrar_mensagem("Você e seu adversário usaram habilidades de defesa ou esquiva, nada aconteceu")

            else:
                self.__tela_luta.mostrar_mensagem("Você não tem stamina suficiente para usar essa habilidade")
                self.__tela_luta.mostrar_mensagem("Tente novamente")

            self.__jogadas_usuario.append(habilidade_escolhida_usuario)
            boxeador_usuario.caracteristica.stamina += FightNumbers.STAMINA.value
            boxeador_adversario.caracteristica.stamina += FightNumbers.STAMINA.value
            jogada += 1
            if jogada == 3:
                jogada = 0
                round += 1
                self.__tela_luta.mostrar_mensagem("-------------------")
                if round == (FightNumbers.ROUND.value + 1):
                    self.__tela_luta.mostrar_mensagem(f"Round 3 de 3")
                else:
                    self.__tela_luta.mostrar_mensagem(f"Round {round} de 3")
                self.__tela_luta.mostrar_mensagem("     FIGHT!!")
                self.__tela_luta.mostrar_mensagem("-------------------")

            if round == (FightNumbers.ROUND.value + 1) or boxeador_usuario.caracteristica.vida <= 0 or boxeador_adversario.caracteristica.vida <= 0:
                self.__tela_luta.mostrar_mensagem("O jogo acabou")
                if boxeador_usuario.caracteristica.vida > boxeador_adversario.caracteristica.vida:
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_usuario.apelido} ganhou a luta")
                    self.mostrar_vitoria_boxeador_um(boxeador_usuario, boxeador_adversario)
                    self.__vitoria_boxeador_usuario = True
                elif boxeador_usuario.caracteristica.vida < boxeador_adversario.caracteristica.vida:
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} ganhou a luta")
                    self.mostrar_vitoria_boxeador_dois(boxeador_usuario, boxeador_adversario)
                else:
                    self.__tela_luta.mostrar_mensagem("Empate")
                    cara_coroa = randint(0, 1)
                    self.__tela_luta.mostrar_mensagem("Jogo será decidido no cara ou coroa")
                    if cara_coroa == 0:
                        self.__tela_luta.mostrar_mensagem(f"O {boxeador_usuario.apelido} ganhou a luta")
                        self.mostrar_vitoria_boxeador_um(boxeador_usuario, boxeador_adversario)
                        self.__vitoria_boxeador_usuario = True
                    else:
                        self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} ganhou a luta")
                        self.mostrar_vitoria_boxeador_dois(boxeador_usuario, boxeador_adversario)
                return self.__vitoria_boxeador_usuario, self.__jogadas_usuario, _dano_causado_usuario

    def organizar_campeonato(self, fase, jogador_usuario, jogador_adversario):
        if fase == 'semi-final':
            luta_final = self.__controlador_central.controlador_torneio.lutas
            jogador_adversario = luta_final[FightNumbers.MYKE_TYSON.value].boxeador_dois
            self.__tela_luta.mostrar_final(jogador_usuario, jogador_adversario)
            self.__controlador_central.controlador_torneio.mostrar_luta_usuario(boxeador_um=jogador_usuario,
                                                                                boxeador_dois=jogador_adversario)
            luta_dois, lista_jogadas_usuario, dano_total_causado = self.iniciar_luta(jogador_usuario,
                                                                                     jogador_adversario)
            if luta_dois:
                self.__tela_luta.mostrar_campeao(jogador_usuario)
                self.retorna_informacoes_lista(lista_jogadas_usuario, dano_total_causado)
                self.__controlador_central.inicializa_sistema()
            else:
                self.__tela_luta.mostrar_campeao(jogador_adversario)
                self.__controlador_central.inicializa_sistema()
        elif fase == 'quartas-de-final':
            self.__tela_luta.mostrar_semi_final(jogador_usuario, jogador_adversario)
            luta_semi_final = self.__controlador_central.controlador_torneio.lutas
            jogador_adversario = luta_semi_final[FightNumbers.TONY_TUCKER.value].boxeador_dois
            self.__tela_luta.mostrar_final(jogador_usuario, jogador_adversario)
            self.__controlador_central.controlador_torneio.mostrar_luta_usuario(boxeador_um=jogador_usuario,
                                                                                boxeador_dois=jogador_adversario)
            luta_dois, lista_jogadas_usuario, dano_total_causado = self.iniciar_luta(jogador_usuario,
                                                                                     jogador_adversario)
            if luta_dois:
                self.__tela_luta.mostrar_mensagem("Você passou para a final")
                self.retorna_informacoes_lista(lista_jogadas_usuario, dano_total_causado)
                luta_final = self.__controlador_central.controlador_torneio.lutas
                jogador_adversario = luta_final[FightNumbers.MYKE_TYSON.value].boxeador_dois
                self.__tela_luta.mostrar_final(jogador_usuario, jogador_adversario)
                self.__controlador_central.controlador_torneio.mostrar_luta_usuario(boxeador_um=jogador_usuario,
                                                                                    boxeador_dois=jogador_adversario)
                luta_dois, lista_jogadas_usuario, dano_total_causado = self.iniciar_luta(jogador_usuario,
                                                                                         jogador_adversario)
                if luta_dois:
                    self.__tela_luta.mostrar_campeao(jogador_usuario)
                    self.retorna_informacoes_lista(lista_jogadas_usuario, dano_total_causado)
                    self.__controlador_central.inicializa_sistema()
                else:
                    self.__tela_luta.mostrar_campeao(jogador_adversario)
                    self.__controlador_central.inicializa_sistema()

    def escolher_habilidade_cpu(self):
        lista_habilidades = self.__controlador_central.controlador_habilidade.habilidades
        id_escolhido = randint(1, len(lista_habilidades) - 1)
        for habilidades in lista_habilidades:
            if habilidades.id == id_escolhido:
                if habilidades.tipo == 'Ataque':
                    return habilidades
                elif habilidades.tipo == 'Defesa':
                    return habilidades
                elif habilidades.tipo == 'Esquiva':
                    return habilidades
        return None, None

    def busca_por_id(self, id, lista_habilidades):
        for habilidade in lista_habilidades:
            if habilidade.id == id:
                return habilidade
        return None

    def mostrar_luta(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_padrao(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido,
                                          )

    def mostrar_vitoria_boxeador_um(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_um(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido)

    def mostrar_vitoria_boxeador_dois(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_dois(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido)

    def retorna_informacoes_lista(self, lista, dano_total_causado):
        habilidades_usadas = len(lista)
        self.__tela_luta.mostra_informacoes_luta_usuario(dano_total_causado,habilidades_usadas)
