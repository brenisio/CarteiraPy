from Controladores.controlador_boxeador import ControladorBoxeador
from Controladores.controlador_habilidade import ControladorHabilidade
from Controladores.controlador_luta import ControladorLuta
from Controladores.controlador_torneio import ControladorTorneio
from Telas.tela_central import TelaCentral


class ControladorCentral:
    def __init__(self):
        self.__controlador_boxeador = ControladorBoxeador(self)
        self.__controlador_habilidade = ControladorHabilidade(self)
        self.__controlador_luta = ControladorLuta(self)
        self.__controlador_torneio = ControladorTorneio(self)
        self.__tela_central = TelaCentral()


    def inicializa_sistema(self):
        self.cria_base_dados_habilidade()
        self.abre_tela()

    @property
    def controlador_boxeador(self):
        return self.__controlador_boxeador

    @property
    def controlador_habilidade(self):
        return self.__controlador_habilidade

    @property
    def controlador_luta(self):
        return self.__controlador_luta

    @property
    def controlador_torneio(self):
        return self.__controlador_torneio

    def cria_base_dados_habilidade(self):
        self.__controlador_habilidade.gerar_base_de_habilidades()

    def cria_base_dados_boxeador(self):
        self.__controlador_boxeador.gerar_boxeador()
    def cadastra_boxeador(self):
        self.__controlador_boxeador.abre_tela()

    def cadastra_torneio(self):
        self.__controlador_torneio.abre_tela()

    def encerra_sistema(self):
        self.__tela_central.mostrar_mensagem("----------------------------------------------------")
        self.__tela_central.mostrar_mensagem("      Adoramos ter você jogando PUNCH CLUB!!!")
        self.__tela_central.mostrar_mensagem("----------------------------------------------------")
        self.__tela_central.mostrar_mensagem("Com os cumprimentos, Breno Sayão e Cleverson Borges ")
        self.__tela_central.mostrar_mensagem("----------------------------------------------------")
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_boxeador,
                        2: self.__controlador_torneio.abre_tela,
                        3: self.__controlador_luta.iniciar_jogo,
                        0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_central.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            if opcao_escolhida == 0:
                break
