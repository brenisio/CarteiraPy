class Usuario:
    def __init__(self, nome:str, cpf:int, data_nascimento: str = None):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self,data_nascimento):
        self.__data_nascimento = data_nascimento

