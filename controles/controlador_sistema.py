from controles.controlador_usuario import ControladorUsuario
from controles.controlador_ativo import ControladorAtivo
from controles.controlador_conta import ControladorConta
from controles.controlador_ordem import ControladorOrdem
from telas.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_ativo = ControladorAtivo(self)
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_ordem = ControladorOrdem(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_ativo(self):
        return self.__controlador_ativo

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    @property
    def controlador_ordem(self):
        return self.__controlador_ordem

    def cadastra_ativo(self):
        self.__controlador_ativo.abre_tela()

    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()

    def cadastra_conta(self):
        self.__controlador_conta.abre_tela_login()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario,
                        2: self.cadastra_ativo,
                        3: self.cadastra_conta,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()