from entidades.ativo import Ativo
from telas.tela_ativo import TelaAtivo
from DAOs.ativo_dao import AtivoDAO
from exceptions.lista_vazia_exception import ListaVaziaError


class ControladorAtivo:
    def __init__(self, controlador_sistema):
        self.__ativo_DAO = AtivoDAO()
        self.__tela_ativo = TelaAtivo()
        self.__controlador_sistema = controlador_sistema

    def busca_por_id(self, identificador:str):
        for ativo in self.__ativo_DAO.get_all():
            if(ativo.identificador == identificador):
                return ativo
        return False

    def cadastrar_ativo(self):
        dados_ativo = self.__tela_ativo.cadastrar_ativo()
        if dados_ativo == 1:
            self.encerra_sistema()
        if dados_ativo == 0:
            self.__tela_ativo.print_mensagem("O valor mínimo deve ser número")
            self.encerra_sistema()
        if dados_ativo is not False:
            ativo = Ativo(dados_ativo["nome"],
                          dados_ativo["valor_min"],
                          dados_ativo["identificador"],
                          dados_ativo["tipo_investimento"],
                          dados_ativo["resumo"])

            verificar_id = self.busca_por_id(dados_ativo["identificador"])
            if verificar_id is not False:
                self.__tela_ativo.print_mensagem('Já existe Ativo com este identificador')
                self.cadastrar_ativo()

            self.__ativo_DAO.add(ativo)
        else:
            self.__tela_ativo.print_mensagem('VOCÊ NÃO PREENCHEU TODOS OS CAMPOS, O ATIVO NÃO FOI CADASTRADO')
            self.cadastrar_ativo()

    def listar_ativos(self):
        ativos_cadastrados = []
        try:
            if len(self.__ativo_DAO.get_all()) > 0:
                for ativo in self.__ativo_DAO.get_all():
                    ativos_cadastrados.append({ "nome": ativo.nome,
                                                "valor_min": ativo.valor_min,
                                                "identificador": ativo.identificador,
                                                "tipo_investimento": ativo.tipo_investimento,
                                                "resumo": ativo.resumo})
                self.__tela_ativo.mostra_ativo(ativos_cadastrados)
            else:
                raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_ativo.print_mensagem(error)

    def alterar_ativo(self):
        try:
            if len(self.__ativo_DAO.get_all()) > 0:
                self.listar_ativos()
                identificador_ativo = self.__tela_ativo.seleciona_por_identificador()
                ativo = self.busca_por_id(identificador_ativo)
                if (ativo is not False):
                    novos_dados = self.__tela_ativo.cadastrar_ativo()
                    ativo.nome = novos_dados["nome"]
                    ativo.valor_min = novos_dados["valor_min"]
                    ativo.identificador = novos_dados["identificador"]
                    ativo.tipo_investimento = novos_dados["tipo_investimento"]
                    ativo.resumo = novos_dados["resumo"]
                    self.__ativo_DAO.update(ativo)
                    self.listar_ativos()
                else:
                    self.__tela_ativo.print_mensagem("CUIDADO: ESTE ATIVO NÃO EXISTE")
            else:
                    raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_ativo.print_mensagem(error)


    def remover_ativo(self):
        try:
            if len(self.__ativo_DAO.get_all()) > 0:
                self.listar_ativos()
                identificador_ativo = self.__tela_ativo.seleciona_por_identificador()
                ativo = self.busca_por_id(identificador_ativo)
                if (ativo is not False):
                    self.__ativo_DAO.remove(ativo.identificador)
                    self.listar_ativos()
                else:
                    self.__tela_ativo.print_mensagem("CUIDADO: ESTE ATIVO NÃO EXISTE")
            else:
                raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_ativo.print_mensagem(error)

    def encerra_sistema(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):

        escolha_tela = {1: self.listar_ativos,
                        2: self.cadastrar_ativo,
                        3: self.alterar_ativo,
                        4: self.remover_ativo,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_ativo.tela_opcoes()]()