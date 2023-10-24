class Ativo:
    def __init__(self, nome: str, valor_min: int, identificador: str, tipo_investimento: str, resumo: str):
        self.__nome = nome
        self.__valor_min = valor_min
        self.__identificador = identificador
        self.__tipo_investimento = tipo_investimento
        self.__resumo = resumo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor_min(self):
        return self.__valor_min

    @valor_min.setter
    def valor_min(self, valor_min):
        self.__valor_min = valor_min

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def tipo_investimento(self):
        return self.__tipo_investimento

    @tipo_investimento.setter
    def tipo_investimento(self, tipo_investimento):
        self.__tipo_investimento = tipo_investimento

    @property
    def resumo(self):
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo