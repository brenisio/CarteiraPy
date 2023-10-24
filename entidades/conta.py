from entidades.usuario import Usuario

class Conta(Usuario):
    def __init__(self, nome:str, cpf:int, senha:int, id_conta:str, tipo_perfil:str, saldo:int):#, usuario:Usuario):
        super().__init__(nome, cpf)
        self.__senha = senha
        self.__id_conta = id_conta
        self.__tipo_perfil = tipo_perfil
        self.__saldo = saldo
        # if isinstance(usuario, Usuario):
        #     self.__dono = usuario
        self.__ativos_conta = []

    # def adicionar_ativo(self, ativo):
    #     print(self.__senha)

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def id_conta(self):
        return self.__id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        self.__id_conta = id_conta

    @property
    def tipo_perfil(self):
        return self.__tipo_perfil

    @tipo_perfil.setter
    def tipo_perfil(self, tipo_perfil):
        self.__tipo_perfil = tipo_perfil

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def ativos_conta(self):
        return self.__ativos_conta

    @ativos_conta.setter
    def ativos_conta(self, ativos_conta):
        self.__ativos_conta = ativos_conta