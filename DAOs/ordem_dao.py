from DAOs.dao import DAO
from entidades.conta import Conta
from entidades.ativo import Ativo
from entidades.ordem import Ordem


#cada entidade terá uma classe dessa, implementação bem simples.
class OrdemDAO(DAO):
    def __init__(self):
        super().__init__('ordens.pkl')

    def add(self, ordem: Ordem):
        if((ordem is not None) and isinstance(ordem, Ordem) and isinstance(ordem.ativo, Ativo) and isinstance(ordem.conta, Conta)):
            super().add(ordem.ativo, ordem)

    def update(self, ordem: Ordem):
        if ((ordem is not None) and isinstance(ordem, Ordem) and isinstance(ordem.ativo, Ativo) and isinstance(ordem.conta, Conta)):
            super().add(ordem.ativo, ordem)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)