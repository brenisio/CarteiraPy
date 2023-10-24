from entidades.ativo import Ativo
from entidades.conta import Conta
from datetime import datetime
from random import randint


class Ordem:
    def __init__(self, ativo:Ativo, conta:Conta, estado_aquisicao:str):
        if isinstance(conta, Conta):
            self.__conta = conta
        if isinstance(ativo, Ativo):
            self.__ativo = ativo
        self.__estado_aquisicao = estado_aquisicao
        self.__id_ordem = randint(1,999)
        self.__data_aquisicao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def estado_aquisicao(self):
        return self.__estado_aquisicao

    @estado_aquisicao.setter
    def estado_aquisicao(self, estado_aquisicao):
        self.__estado_aquisicao = estado_aquisicao

    @property
    def id_ordem(self):
        return self.__id_ordem

    @id_ordem.setter
    def id_ordem(self, id_ordem):
        self.__id_ordem = id_ordem

    @property
    def data_aquisicao(self):
        return self.__data_aquisicao

    @data_aquisicao.setter
    def data_aquisicao(self, data_aquisicao):
        self.__data_aquisicao = data_aquisicao