import PySimpleGUI as sg


class TelaOrdem:
    def __init__(self):
        self.__window = None
        self.init_opcoes_ordem()

    def init_opcoes_ordem(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ ORDEM █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Listar ordens', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Consultar ordem', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Cancelar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Consultar Ordens').Layout(layout)

    def tela_ordem_opcoes(self):
        self.init_opcoes_ordem()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def seleciona_por_identificador_ordem(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONAR ATIVO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o identificador da ordem que deseja buscar: ', font=("Lucida", 15))],
            [sg.Text('id_ordem:', size=(15, 1)), sg.InputText('', key='id_ordem')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona id_ordem').Layout(layout)

        button, values = self.open()
        id_ordem = values['id_ordem']
        self.close()
        return id_ordem

    def mostra_ordem(self, dados_ordem):
        string_todos_ordem = ""
        for ordem in dados_ordem:
            string_todos_ordem = string_todos_ordem + "IDENTIFICADOR DO ATIVO: " + ordem["ativo"] + '\n'
            string_todos_ordem = string_todos_ordem + "VALOR DE COMPRA DO ATIVO: " + ordem["valor"] + '\n'
            string_todos_ordem = string_todos_ordem + "NOME DO COMPRADOR: " + ordem["nome"] + '\n'
            string_todos_ordem = string_todos_ordem + "ID_CONTA: " + ordem["id_conta"] + '\n'
            string_todos_ordem = string_todos_ordem + "ESTADO DE AQUISIÇÃO: " + ordem["estado_aquisicao"] + '\n'
            string_todos_ordem = string_todos_ordem + "RESUMO INVESTIMENTO: " + ordem["resumo"] + '\n'
            string_todos_ordem = string_todos_ordem + "ID ORDEM: " + str(ordem["id_ordem"]) + '\n'
            string_todos_ordem = string_todos_ordem + "DATA E HORA: " + ordem["data_aquisicao"] + '\n'
            string_todos_ordem = string_todos_ordem + '\n'

        sg.Popup('░▒▓█ LISTA DE ORDENS █▓▒░', string_todos_ordem)

    def consultar_ordem(self, dados_ordem):
        string_todos_ordem = ""
        for ordem in dados_ordem:
            string_todos_ordem = string_todos_ordem + "NOME DO ATIVO: " + ordem["nome"] + '\n'
            string_todos_ordem = string_todos_ordem + "IDENTIFICADOR DO ATIVO: " + ordem["ativo"] + '\n'
            string_todos_ordem = string_todos_ordem + "VALOR DE COMPRA DO ATIVO: " + ordem["valor"] + '\n'
            string_todos_ordem = string_todos_ordem + "ID_CONTA: " + ordem["id_conta"] + '\n'
            string_todos_ordem = string_todos_ordem + "TIPO DE PERFIL DO USUÁRIO: " + ordem["tipo_perfil"] + '\n'
            string_todos_ordem = string_todos_ordem + "ESTADO DE AQUISIÇÃO: " + ordem["estado_aquisicao"] + '\n'
            string_todos_ordem = string_todos_ordem + "RESUMO INVESTIMENTO: " + ordem["id_ordem"] + '\n'
            string_todos_ordem = string_todos_ordem + "DATA E HORA: " + ordem["data_aquisicao"] + '\n'
            string_todos_ordem = string_todos_ordem + '\n'

        sg.Popup('░▒▓█ CONSULTAR ORDEM █▓▒░', string_todos_ordem)

    def print_mensagem(self, mensagem):
        sg.popup("", mensagem)