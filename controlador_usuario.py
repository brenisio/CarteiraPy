from datetime import datetime
from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario
from DAOs.usuario_dao import UsuarioDAO
from exceptions.lista_vazia_exception import ListaVaziaError
from exceptions.menor_de_idade_exception import MenorIdadeError


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuario_DAO = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def verificar_maioridade(self, dia, mes, ano):
        # Verifica se uma pessoa é maior de idade com base na data de nascimento
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if ano <= 1910:
            return 0
        if mes < 1 or mes > 12:
            return 0
        if dia < 1 or dia > 31:
            return 0
        data_nascimento = datetime(ano, mes, dia)
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year

        if data_atual.month < data_nascimento.month or (
                data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
            idade -= 1

        if idade >= 18:
            return True
        else:
            return False

    def busca_por_cpf(self, cpf:int):
        for usuario in self.__usuario_DAO.get_all():
            if(usuario.cpf == cpf):
                return usuario
        return False

    def incluir_usuario(self):
        dados_usuario = self.__tela_usuario.cadastrar_usuario()
        if dados_usuario == 1:
            self.encerra_sistema()
        if dados_usuario == 0:
            self.__tela_usuario.print_mensagem("O CPF só deve conter números")
            self.encerra_sistema()
        try:
            if dados_usuario is not False:
                maioridade = self.verificar_maioridade(dados_usuario["dia_nascimento"],
                                                       dados_usuario["mes_nascimento"],
                                                       dados_usuario["ano_nascimento"])

                if maioridade == 0:
                    return self.__tela_usuario.print_mensagem("Você colocou algum número inválido na data de nascimento")
                elif maioridade == False:
                    raise MenorIdadeError

                usuario = Usuario(dados_usuario["nome"],
                                  int((dados_usuario["cpf"])),
                                  dados_usuario["data_nascimento"])

                cpf = self.busca_por_cpf(dados_usuario["cpf"])
                if cpf is not False:
                    self.__tela_usuario.print_mensagem('Já existe Usuário com este CPF')
                    self.incluir_usuario()

                self.__usuario_DAO.add(usuario)
            else:
                self.__tela_usuario.print_mensagem('VOCÊ NÃO PREENCHEU TODOS OS CAMPOS, O USUÁRIO NÃO FOI CADASTRADO')
                self.incluir_usuario()
        except MenorIdadeError as e:
            self.__tela_usuario.print_mensagem(e)

    def listar_usuarios(self):
        try:
            usuarios_cadastrados = []
            if len(self.__usuario_DAO.get_all()) > 0:
                for usuario in self.__usuario_DAO.get_all():
                    usuarios_cadastrados.append({"nome":usuario.nome,
                                                    "cpf":usuario.cpf,
                                                    "data_nascimento":usuario.data_nascimento})
                self.__tela_usuario.mostra_usuario(usuarios_cadastrados)
            else:
                raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_usuario.print_mensagem(error)

    def alterar_usuario(self):
        try:
            if len(self.__usuario_DAO.get_all()) > 0:
                self.listar_usuarios()
                cpf_usuario = self.__tela_usuario.seleciona_por_cpf()
                if cpf_usuario == 0:
                    self.encerra_sistema()
                elif cpf_usuario == False:
                    self.__tela_usuario.print_mensagem("Você não digitou nada no CPF")
                usuario = self.busca_por_cpf(cpf_usuario)

                if (usuario is not False):
                    novos_dados = self.__tela_usuario.cadastrar_usuario()
                    maioridade = self.verificar_maioridade(novos_dados["dia_nascimento"],
                                                           novos_dados["mes_nascimento"],
                                                           novos_dados["ano_nascimento"])

                    if maioridade == 0:
                        return self.__tela_usuario.print_mensagem("Você colocou algum número inválido na data de nascimento")
                    elif maioridade == False:
                        raise MenorIdadeError

                    usuario.nome = novos_dados["nome"]
                    usuario.cpf = novos_dados["cpf"]
                    usuario.data_nascimento = novos_dados["data_nascimento"]
                    self.__usuario_DAO.update(usuario)
                    self.listar_usuarios()
                else:
                    self.__tela_usuario.print_mensagem("CUIDADO: NÃO EXISTE USUÁRIO COM ESTE CPF")
            else:
                raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_usuario.print_mensagem(error)
        except MenorIdadeError as error:
            self.__tela_usuario.print_mensagem(error)

    def excluir_usuario(self):
        try:
            if len(self.__usuario_DAO.get_all()) > 0:
                self.listar_usuarios()
                cpf_usuario = self.__tela_usuario.seleciona_por_cpf()
                usuario = self.busca_por_cpf(cpf_usuario)

                if (usuario is not False):
                    self.__usuario_DAO.remove(usuario.cpf)
                    self.listar_usuarios()
                else:
                    self.__tela_usuario.print_mensagem("CUIDADO: NÃO EXISTE USUÁRIO COM ESTE CPF")
            else:
                raise ListaVaziaError
        except ListaVaziaError as error:
            self.__tela_usuario.print_mensagem(error)

    def encerra_sistema(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        escolha_tela = {1: self.listar_usuarios, 2: self.incluir_usuario, 3: self.alterar_usuario, 4: self.excluir_usuario, 0:self.encerra_sistema}
        continua = True
        while continua:
            escolha_tela[self.__tela_usuario.tela_opcoes()]()