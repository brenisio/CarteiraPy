from Telas.tela_torneio import TelaTorneio
from Entidades.luta import Luta
from Entidades.torneio import Torneio
from DAOs.torneio_dao import TorneioDAO
import random


class ControladorTorneio:
    def __init__(self, controlador_central, torneio_atual=None, lutas=None, torneio_criado=False):
        self.__controlador_central = controlador_central
        self.__tela_torneio = TelaTorneio()
        self.__torneio_atual = torneio_atual
        self.__lutas = lutas if lutas is not None else []
        self.__torneio_criado = torneio_criado
        self.__fase_atual = None

    @property
    def lutas(self):
        return self.__lutas

    @property
    def torneio_atual(self):
        return self.__torneio_atual

    @property
    def torneio_criado(self):
        return self.__torneio_criado

    @property
    def fase_atual(self):
        return self.__fase_atual

    def cadastrar_torneio(self):
        if len(self.__controlador_central.controlador_boxeador.boxeadores) > 0:
            self.__controlador_central.controlador_boxeador.gerar_boxeador()
            self.__controlador_central.controlador_boxeador.bonificacao_por_peso()
            if self.__torneio_criado:
                self.__tela_torneio.mostrar_mensagem("Torneio já cadastrado, se quiser altere-o!")
            else:
                informacoes_torneio = self.__tela_torneio.cadastro_torneio()
                nome_torneio = informacoes_torneio["nome_torneio"]
                numero_lutadores = informacoes_torneio["numero_lutadores"]
                numero_lutas = numero_lutadores / 2
                if numero_lutas == 4:
                    self.__fase_atual = 'semi-final'
                elif numero_lutas == 8:
                    self.__fase_atual = 'quartas-de-final'
                self.__torneio_atual = Torneio(nome_torneio, numero_lutas)
                self.criar_lutas(self.__torneio_atual.numero_lutas)
                self.__torneio_criado = True
                self.__tela_torneio.mostrar_mensagem("                                                              ")
                self.__tela_torneio.mostrar_mensagem("------------------------TORNEIO CRIADO------------------------")
                self.__tela_torneio.mostrar_mensagem("                                                              ")

                self.mostrar_torneio()
        else:
            self.__tela_torneio.mostrar_mensagem("------------------------------ATENÇÃO------------------------------")
            self.__tela_torneio.mostrar_mensagem("Não há boxeadores cadastrados, é necessário cadastrar boxeadores antes")
            self.__tela_torneio.mostrar_mensagem("------------------------------------------------------------------")

    def alterar_torneio(self):
        if self.__torneio_atual:
            informacoes_torneio = self.__tela_torneio.alterar_torneio()
            nome_torneio = informacoes_torneio["nome_torneio"]
            self.__torneio_atual.nome_torneio = nome_torneio
        else:
            self.__tela_torneio.mostrar_mensagem("Não há nenhum torneio cadastrado para editar")
    def mostrar_torneio(self):
        if self.__torneio_atual:
            self.__tela_torneio.mostrar_torneio(self.__torneio_atual.nome_torneio, int(self.__torneio_atual.numero_lutas * 2))
            for luta in self.__lutas:
                self.__tela_torneio.mostrar_chaveamento(self.__torneio_atual.nome_torneio, luta.boxeador_um, luta.boxeador_dois, self.__torneio_atual.numero_lutas)
        else:
            self.__tela_torneio.mostrar_mensagem("Torneio não cadastrado, é necessário cadastrar o torneio antes")
    def criar_lutas(self, numero_lutadores):
        lista_boxeadores = self.__controlador_central.controlador_boxeador.boxeadores
        numero_lutadores = int(numero_lutadores * 2)
        lista_boxeadores = lista_boxeadores[:(numero_lutadores)]
        contador = 0
        while contador < (len(lista_boxeadores) - 1):
            lutador_um = lista_boxeadores[contador]
            lutador_dois = lista_boxeadores[contador + 1]
            contador = contador + 2
            self.__lutas.append(Luta(lutador_um, lutador_dois))

    def mostrar_luta_usuario(self, boxeador_um, boxeador_dois):
        self.__tela_torneio.mostrar_luta_usuario(self.torneio_atual.nome_torneio,boxeador_um, boxeador_dois)

    def gerar_lutas(self):
        lista_boxeadores = self.__controlador_central.controlador_boxeador.boxeadores
        for boxeador in range(lista_boxeadores):
            boxeador1, boxeador2 = random.sample(lista_boxeadores, 2)
            return boxeador1, boxeador2

    def mostrar_chaveamento(self):
        for luta in self.__lutas:
            self.__tela_torneio.mostrar_chaveamento(self.__torneio_atual.nome_torneio, luta.boxeador_um, luta.boxeador_dois, luta.fase)
    def encerra_sistema(self):
        self.__controlador_central.abre_tela()

    def abre_tela(self):

        escolha_tela = {1: self.cadastrar_torneio,
                        2: self.alterar_torneio,
                        3: self.mostrar_torneio,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_torneio.tela_opcoes()]()
