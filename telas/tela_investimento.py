from controles.controlador_ativo import ControladorInvestimento

class TelaInvestimento:
    def __int__(self, controlador: ControladorInvestimento):
        if not isinstance(controlador,ControladorInvestimento):
            raise TypeError("Controlador tem de ser um objeto da classe ControladorInvestimento")

        self.__controlador = controlador

    def cadastrar_investimento(self):
        pass
