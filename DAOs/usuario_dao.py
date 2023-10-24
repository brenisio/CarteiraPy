from DAOs.dao import DAO
from entidades.usuario import Usuario

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.cpf, int)):
            super().add(usuario.cpf, usuario)

    def update(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.cpf, int)):
            super().update(usuario.cpf, usuario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)