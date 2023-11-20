from entidades.ordem import Ordem
from telas.tela_ordem import TelaOrdem
from DAOs.ordem_dao import OrdemDAO
from exceptions.lista_vazia_exception import ListaVaziaError


class ControladorOrdem:
    def __init__(self, controlador_sistema):
        self.__ordem_DAO = OrdemDAO()
        self.__tela_ordem = TelaOrdem()
        self.__controlador_sistema = controlador_sistema

    def busca_por_id(self, identificador:str):
        for ordem in self.__ordem_DAO.get_all():
            if(ordem.id_ordem == identificador):
                return ordem
        return False

    def cadastrar_ordem(self, dados_ordem):
        if dados_ordem is not False:
            ordem = Ordem(dados_ordem.ativo,
                          dados_ordem.conta,
                          dados_ordem.estado_aquisicao)

            self.__ordem_DAO.add(ordem)

    def listar_ordens(self, conta_recebida):
        try:
            ordens_criadas = []
            if len(self.__ordem_DAO.get_all()) > 0:
                for ordem in self.__ordem_DAO.get_all():
                    if ordem.conta.id_conta == conta_recebida.id_conta:
                        ordens_criadas.append({ "ativo": ordem.ativo.identificador,
                                                "valor": ordem.ativo.valor_min,
                                                "resumo":ordem.ativo.resumo,
                                                "id_conta": ordem.conta.id_conta,
                                                "nome": ordem.conta.nome,
                                                "estado_aquisicao": ordem.estado_aquisicao,
                                                "id_ordem": ordem.id_ordem,
                                                "data_aquisicao": ordem.data_aquisicao})
                    else:
                        self.__tela_ordem.print_mensagem("Não tem nenhuma ordem nesta conta")
                        return False
                self.__tela_ordem.mostra_ordem(ordens_criadas)
            else:
                raise ListaVaziaError("Não há nenhuma ordem cadastrada")
        except ListaVaziaError as error:
            self.__tela_ordem.print_mensagem(error)


    def consultar_ordem(self):
        try:
            id_ordem = self.__tela_ordem.seleciona_por_identificador_ordem()
            ordens_criadas = []
            if len(self.__ordem_DAO.get_all()) == 0:

                for ordem in self.__ordem_DAO.get_all():
                    if ordem.id_ordem == id_ordem:
                        ordens_criadas.append({ "nome": ordem.ativo.nome,
                                                "ativo": ordem.ativo.identificador,
                                                "valor": ordem.ativo.valor_min,
                                                "identificador": ordem.ativo.id_conta,
                                                "tipo_investimento": ordem.ativo.tipo_investimento,
                                                "resumo": ordem.ativo.resumo,
                                                "id_conta": ordem.conta.id_conta,
                                                "tipo_perfil": ordem.conta.tipo_perfil,
                                                "estado_aquisicao": ordem.estado_aquisicao,
                                                "id_ordem": ordem.id_ordem,
                                                "data_aquisicao": ordem.data_aquisicao})
                    else:
                        self.__tela_ordem.print_mensagem("Não tem nenhuma ordem nesta conta")
                        return False
                self.__tela_ordem.mostra_ordem(ordens_criadas)
            else:
                raise ListaVaziaError("Não há nenhuma ordem cadastrada")
        except ListaVaziaError as error:
            self.__tela_ordem.print_mensagem(error)

    def encerra_sistema(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_ordem(self):
        continua = True
        escolha_tela = {1: self.listar_ordens,
                        2: self.consultar_ordem,
                        0: self.encerra_sistema}
        while continua:
            escolha_tela[self.__tela_ordem.tela_ordem_opcoes()]()