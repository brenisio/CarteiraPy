from entidades.conta import Conta
from telas.tela_conta import TelaConta
from DAOs.conta_dao import ContaDAO
from entidades.ordem import Ordem
from exceptions.lista_vazia_exception import ListaVaziaError


class ControladorConta:
    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela_conta = TelaConta()
        self.__conta_DAO = ContaDAO()
        self.__numero_registro_conta = 1
        self.__conta_atual = None

    def busca_por_id_conta(self, id_conta):
        for conta in self.__conta_DAO.get_all():
            if(conta.id_conta == id_conta):
                return conta
        return False

    def verificar_senha_conta(self, senha):
        for conta in self.__conta_DAO.get_all():
            if(conta.senha["senha"] == senha):
                return True
        return False

    def depositar(self):
        valor = self.__tela_conta.insere_valor()
        if valor <= 0 or valor == False:
            self.__tela_conta.print_mensagem("Revise o valor do depósito, não podemos proceder com este valor.")
        else:
            if (self.__conta_atual is not None):
                self.__conta_atual.saldo = self.__conta_atual.saldo + int(valor)
                self.__tela_conta.print_mensagem(f"Depósito de {valor}R$ na conta {self.__conta_atual.id_conta}")
                self.__conta_DAO.update(self.__conta_atual)

    def sacar(self):
        if self.__conta_atual is not None:
            if self.__conta_atual.saldo > 0:
                valor = int(self.__tela_conta.insere_valor())
                if valor <= self.__conta_atual.saldo:
                    self.__conta_atual.saldo = self.__conta_atual.saldo - valor
                    self.__tela_conta.print_mensagem(f"Saque de {valor}R$ na conta {self.__conta_atual.id_conta}")
                    self.__conta_DAO.update(self.__conta_atual)
                else:
                    self.__tela_conta.print_mensagem("Saldo insuficiente")
            else:
                self.__tela_conta.print_mensagem("Não é possível realizar saques. Saldo zero.")
        else:
            self.__tela_conta.print_mensagem("Conta não encontrada")

    def pegar_ativo(self):
        self.__tela_conta.print_mensagem("Escolha o ativo que você deseja comprar")
        self.__controlador_sistema.controlador_ativo.listar_ativos()
        identificador = self.__tela_conta.insere_identificador_ativo()
        ativo = self.__controlador_sistema.controlador_ativo.busca_por_id(identificador)
        return ativo

    def vender_ativo(self):
        self.__tela_conta.print_mensagem("Escolha o ativo que você deseja vender")
        self.listar_ativos_conta()
        identificador = self.__tela_conta.insere_identificador_ativo()
        ativo = self.busca_por_ativo_conta(identificador)
        return ativo

    def adicionar_ativo_para_carteira(self):
        dados_ativo = self.pegar_ativo()
        if dados_ativo is not None:
            valor_minimo = int(dados_ativo.valor_min)
            if self.__conta_atual.saldo >= valor_minimo:  # Verifica se o saldo da conta é maior ou igual ao valor mínimo do ativo
                self.__conta_atual.saldo -= valor_minimo  # Diminui o saldo pelo valor mínimo do ativo
                conta_atual = self.__conta_atual
                dados_ordem = Ordem(dados_ativo,conta_atual, 'Compra')
                self.__controlador_sistema.controlador_ordem.cadastrar_ordem(dados_ordem)
                self.__conta_atual.ativos_conta.append(dados_ativo)
                self.__conta_DAO.update(self.__conta_atual)
                self.__tela_conta.print_mensagem("Ativo adicionado com sucesso!")
                self.listar_ativos_conta()
            else:
                self.__tela_conta.print_mensagem("Saldo insuficiente para adquirir o ativo")
        else:
            self.__tela_conta.print_mensagem("Identificador inválido")

    def vender_ativo_da_carteira(self):
        dados_ativo = self.vender_ativo()
        if dados_ativo is not None:
            valor_ativo = int(dados_ativo.valor_min)
            self.__conta_atual.saldo += valor_ativo  # Diminui o saldo pelo valor mínimo do ativo
            conta_atual = self.__conta_atual
            dados_ordem = Ordem(dados_ativo,conta_atual, 'Venda')
            self.__controlador_sistema.controlador_ordem.cadastrar_ordem(dados_ordem)
            self.__conta_atual.ativos_conta.remove(dados_ativo)
            self.__conta_DAO.update(self.__conta_atual)
            self.__tela_conta.print_mensagem("Ativo vendido com sucesso!")
            self.listar_ativos_conta()
        else:
            self.__tela_conta.print_mensagem("Identificador inválido")

    def consultar_saldo(self):
        conta = self.__conta_atual
        if (conta is not None):
            self.__tela_conta.print_mensagem(f"Seu saldo é de {conta.saldo}R$")
            return conta.saldo

    def fazer_login(self):
        try:
            if len(self.__conta_DAO.get_all()) > 0:
                id_conta, senha = self.__tela_conta.fazer_login()
                if self.busca_por_id_conta(id_conta) is not False and self.verificar_senha_conta(senha) is not False:
                    dados_conta = self.busca_por_id_conta(id_conta)
                    self.__conta_atual = dados_conta
                    self.__tela_conta.print_mensagem("Login bem-sucedido!")
                    return True
                self.__tela_conta.print_mensagem("Login falhou. Nome da conta ou senha incorretos.")
                return False
            else:
                raise ListaVaziaError('Não há conta registrada. Crie uma conta antes')
        except ListaVaziaError as error:
            self.__tela_conta.print_mensagem(error)

    def listar_ativos_conta(self):
        try:
            ativos_conta = []
            if len(self.__conta_DAO.get_all()) > 0:
                for atributo in self.__conta_DAO.get_all():
                    if self.__conta_atual.id_conta == atributo.id_conta:
                        for ativo in atributo.ativos_conta:
                            ativos_conta.append({"nome": ativo.nome,
                                                            "valor_min": ativo.valor_min,
                                                            "identificador": ativo.identificador,
                                                            "tipo_investimento": ativo.tipo_investimento,
                                                            "resumo": ativo.resumo})
                        self.__tela_conta.mostra_ativos_conta(ativos_conta)
            else:
                raise ListaVaziaError()
        except ListaVaziaError as error:
            self.__tela_conta.print_mensagem(error)

    def verifica_conta_existente(self, cpf):
        try:
            if len(self.__conta_DAO.get_all()) > 0:
                for usuario in self.__conta_DAO.get_all():
                    if usuario.cpf == cpf:
                        return True
                return False
            else:
                raise ListaVaziaError('Não há conta registrada')
        except ListaVaziaError as error:
            self.__tela_conta.print_mensagem(error)

    def _criar_conta(self):
        self.__tela_conta.print_mensagem("DIGITE O CPF DO USUÁRIO PARA CRIAR A CONTA")
        cpf_conta = self.__tela_conta.seleciona_por_cpf()
        if self.verifica_conta_existente(cpf_conta) is not True:
            if cpf_conta == 'Voltar':
                self.encerra_sistema()
            if cpf_conta is not False:
                cpf_usuario = self.__controlador_sistema.controlador_usuario.busca_por_cpf(cpf_conta)
                if cpf_usuario is not False:
                    nome = cpf_usuario.nome
                    cpf = cpf_usuario.cpf
                    senha = self.__tela_conta.cadastrar_senha()
                    if senha is not False:
                        tipo_perfil = self.__tela_conta.identificar_perfil_investidor()
                        if tipo_perfil == 1:
                            self.encerra_sistema()
                        id_conta = f"conta{self.__numero_registro_conta}_{str(cpf)[:4]}"
                        nova_conta = Conta(nome, cpf, senha, id_conta, tipo_perfil, saldo=0)
                        self.__conta_DAO.add(nova_conta)
                        self._listar_contas()
                        self.__numero_registro_conta = self.__numero_registro_conta + 1
                        self.__tela_conta.print_mensagem(f"Parabéns, sua conta foi criada. Conta: {id_conta}")
                    else:
                        self.__tela_conta.print_mensagem("A senha não foi cadastrada com sucesso")
                        self.encerra_sistema()
                else:
                    self.__tela_conta.print_mensagem("ATENÇÃO: Para fazer o cadastro da conta, deve-se cadastrar o usuário primeiro")
            else:
                self.__tela_conta.print_mensagem("CPF NÃO ENCONTRADO, TENTE NOVAMENTE")
                self._criar_conta()
        else:
            self.__tela_conta.print_mensagem("CPF JÁ CADASTRADO, MODIFIQUE NO CADASTRO DO USUÁRIO")

    def _listar_contas(self):
        try:
            contas_cadastradas = []
            if len(self.__conta_DAO.get_all()) > 0:
                for usuario in self.__conta_DAO.get_all():
                    contas_cadastradas.append({"nome":usuario.nome,
                                                    "cpf":usuario.cpf,
                                                    "id_conta":usuario.id_conta,
                                                    "tipo_perfil":usuario.tipo_perfil,
                                                    "saldo":usuario.saldo
                                                    })
                self.__tela_conta.mostra_conta(contas_cadastradas)
            else:
                raise ListaVaziaError("Nenhuma conta foi cadastrada ainda. Cadastre um usuário e depois uma conta")
        except ListaVaziaError as error:
          self.__tela_conta.print_mensagem(error)

    def busca_por_id(self, identificador:str):
        for conta in self.__conta_DAO.get_all():
            if(conta.id_conta == identificador):
                return conta
        return False

    def busca_por_ativo_conta(self, identificador:str):
        if len(self.__conta_DAO.get_all()) > 0:
            for atributo in self.__conta_DAO.get_all():
                for ativo in atributo.ativos_conta:
                    if ativo.identificador == identificador:
                        return ativo
                    else:
                        return False

    def encerra_sistema(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_login(self):
        continua = True
        while continua:
            opcao_tela = self.__tela_conta.primeira_tela_opcoes()
            if opcao_tela == 0:
                self.encerra_sistema()
            if opcao_tela == 1:
                self._criar_conta()
            if opcao_tela == 2:
                login = self.fazer_login()
                if login == True:
                    self.abre_tela_conta()
                else:
                    self.encerra_sistema()
            if opcao_tela == 3:
                self._listar_contas()

    def listar_ordens(self):
        try:
            if len(self.__conta_DAO.get_all()) > 0:
                self.__controlador_sistema.controlador_ordem.listar_ordens(self.__conta_atual)
            else:
                raise ListaVaziaError("Não há nenhuma ordem")
        except ListaVaziaError as error:
          self.__tela_conta.print_mensagem(error)


    def abre_tela_conta(self):
        continua = True
        escolha_tela = {1: self.consultar_saldo,
                        2: self.depositar,
                        3: self.sacar,
                        4: self.__controlador_sistema.controlador_ativo.listar_ativos,
                        5: self.adicionar_ativo_para_carteira,
                        6: self.vender_ativo_da_carteira,
                        7: self.listar_ativos_conta,
                        8: self.listar_ordens,
                        0: self.encerra_sistema}
        while continua:
            escolha_tela[self.__tela_conta.segunda_tela_opcoes()]()