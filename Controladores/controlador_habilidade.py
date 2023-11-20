from Entidades.habilidade import Habilidade
from Telas.tela_habilidade import TelaHabilidade
from Entidades.ataque import Ataque
from Entidades.defesa import Defesa
from Entidades.esquiva import Esquiva


class ControladorHabilidade:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__habilidades = []
        self.__tela_habilidade = TelaHabilidade()

    @property
    def habilidades(self):
        return self.__habilidades

    def cadastrar_habilidade(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidades.append(habilidade)
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')

    def habilidade_atual(self, habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidade_atual = habilidade
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')

    def gerar_base_de_habilidades(self):
        habilidade1 = Ataque(1, 'Jab', 'Soco direto', 'Ataque', 3, 3)
        habilidade2 = Ataque(2, 'Hook', 'Soco gancho', 'Ataque', 3, 5)
        habilidade3 = Ataque(3, 'Uppercut', 'Soco Uppercut', 'Ataque', 5, 8)
        habilidade4 = Defesa(4, 'Bloqueio', 'Bloqueio de soco', 'Defesa', 3, 35)
        habilidade5 = Defesa(5, 'Cobertura', 'Cobrir a cabeça e o corpo com os braços', 'Defesa', 7, 75)
        habilidade6 = Defesa(6, 'Clinch', 'Segurar o oponente para interromper os ataques', 'Defesa', 8, 90)
        habilidade7 = Esquiva(7, 'Esquiva rápida', 'Esquiva rápida para desviar de socos', 'Esquiva', 5, 20)
        habilidade8 = Esquiva(8, 'Esquiva diagonal', 'Esquiva diagonal para evitar ataques', 'Esquiva', 8, 35)
        habilidade9 = Esquiva(9, 'Esquiva para trás', 'Movimento de recuo para escapar de golpes', 'Esquiva', 10, 55)
        self.__habilidades.append(habilidade1)
        self.__habilidades.append(habilidade2)
        self.__habilidades.append(habilidade3)
        self.__habilidades.append(habilidade4)
        self.__habilidades.append(habilidade5)
        self.__habilidades.append(habilidade6)
        self.__habilidades.append(habilidade7)
        self.__habilidades.append(habilidade8)
        self.__habilidades.append(habilidade9)

    def adicionar_habilidade(self):
        contador = 0
        habilidades_escolhidas = []
        self.__tela_habilidade.mostrar_mensagem('-'*50)
        self.__tela_habilidade.mostrar_mensagem('Adicione 4 habilidades ao seu boxeador')
        self.__tela_habilidade.mostrar_mensagem('-'*50)
        while contador < 4:
            habilidade_escolhida = self.__tela_habilidade.selecionar_tipo()
            if habilidade_escolhida == 0:
                return None
            if habilidade_escolhida == 1:
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.__tela_habilidade.mostrar_mensagem('Habilidades de ataque')
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.busca_habilidade_ataque('Ataque')
                habilidades_escolhidas.append(self.selecao_habilidade_ataque())
                contador += 1
            elif habilidade_escolhida == 2:
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.__tela_habilidade.mostrar_mensagem('Habilidades de defesa')
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.busca_habilidade_defesa('Defesa')
                habilidades_escolhidas.append(self.selecao_habilidade_defesa())
                contador += 1
            elif habilidade_escolhida == 3:
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.__tela_habilidade.mostrar_mensagem('Habilidades de esquiva')
                self.__tela_habilidade.mostrar_mensagem('-'*50)
                self.busca_habilidade_esquiva('Esquiva')
                habilidades_escolhidas.append(self.selecao_habilidade_esquiva())
                contador += 1
            self.__tela_habilidade.mostrar_mensagem('Habilidade adicionada com sucesso!')
        self.__tela_habilidade.mostrar_mensagem('-'*50)
        self.__tela_habilidade.mostrar_mensagem('As habilidades foram cadastras com sucesso!')
        self.__tela_habilidade.mostrar_mensagem('-'*50)
        return habilidades_escolhidas

    def selecao_habilidade_ataque(self):
        id = self.__tela_habilidade.obtem_id_ataque()
        habilidade_escolhida = self.busca_por_id(id)
        if habilidade_escolhida is not None:
            return habilidade_escolhida

    def selecao_habilidade_defesa(self):
        id = self.__tela_habilidade.obtem_id_defesa()
        habilidade_escolhida = self.busca_por_id(id)
        if habilidade_escolhida is not None:
            return habilidade_escolhida

    def selecao_habilidade_esquiva(self):
        id = self.__tela_habilidade.obtem_id_esquiva()
        habilidade_escolhida = self.busca_por_id(id)
        if habilidade_escolhida is not None:
            return habilidade_escolhida
    def busca_por_id(self, id):
        if id == 0:
            self.__tela_habilidade.selecionar_tipo()
        for habilidade in self.habilidades:
            if habilidade.id == id:
                return habilidade
        return None

# Método que pode substiuir outros
#
#    def busca_habilidade(self):
#        for habilidade in self.__habilidades:
#            if habilidade.tipo == 'Ataque':
#                self.__tela_habilidade.mostrar_habilidade_ataque(habilidade)

    def busca_habilidade_ataque(self, tipo):
        for habilidade in self.__habilidades:
            if habilidade.tipo == tipo:
                self.__tela_habilidade.mostrar_habilidade_ataque(habilidade)

    def busca_habilidade_defesa(self, tipo):
        for habilidade in self.__habilidades:
            if habilidade.tipo == tipo:
                self.__tela_habilidade.mostrar_habilidade_defesa(habilidade)

    def busca_habilidade_esquiva(self, tipo):
        for habilidade in self.__habilidades:
            if habilidade.tipo == tipo:
                self.__tela_habilidade.mostrar_habilidade_esquiva(habilidade)
