from DAOs.dao import DAO
from entidades.ativo import Ativo


class AtivoDAO(DAO):
    def __init__(self):
        super().__init__('ativos.pkl')

    def add(self, ativo: Ativo):
        if((ativo is not None) and isinstance(ativo, Ativo) and isinstance(ativo.identificador, str)):
            super().add(ativo.identificador, ativo)

    def update(self, ativo: Ativo):
        if ((ativo is not None) and isinstance(ativo, Ativo) and isinstance(ativo.identificador, str)):
            super().update(ativo.identificador, ativo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)