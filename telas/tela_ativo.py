import PySimpleGUI as sg

class TelaAtivo():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE ATIVO █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Listar Ativos', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Cadastrar Ativo', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Alterar Ativo', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Remover Ativo', size=(25, 2), key='4', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Cancelar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de Ativos').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '4':
            opcao = 4
        # cover the cases of going back, not clicking anything, closing the window, or clicking cancel
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def mostra_ativo(self, dados_ativo):
        string_todos_ativos = ""
        for ativo in dados_ativo:
            string_todos_ativos = string_todos_ativos + "NOME DO ATIVO: " + ativo["nome"] + '\n'
            string_todos_ativos = string_todos_ativos + "VALOR MINIMO DO ATIVO: " + ativo["valor_min"] + '\n'
            string_todos_ativos = string_todos_ativos + "IDENTIFICADOR: " + ativo["identificador"] + '\n'
            string_todos_ativos = string_todos_ativos + "TIPO DO INVESTIMENTO: " + ativo["tipo_investimento"] + '\n'
            string_todos_ativos = string_todos_ativos + "RESUMO INVESTIMENTO: " + ativo["resumo"] + '\n'
            string_todos_ativos = string_todos_ativos + '\n'

        sg.Popup('░▒▓█ LISTA DE ATIVOS █▓▒░', string_todos_ativos)

    def seleciona_por_identificador(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONAR ATIVO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o identificador do ativo que deseja selecionar [Ex: PETR4]:', font=("Lucida", 15))],
            [sg.Text('Identificador:', size=(15, 1)), sg.InputText('', key='identificador')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona ativo').Layout(layout)

        button, values = self.open()
        identificador = values['identificador']
        self.close()
        return identificador

    def cadastrar_ativo(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ DADOS DO ATIVO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Valor mínimo:', size=(15, 1)), sg.InputText('', key='valor_min')],
            [sg.Text('Identificador:', size=(15, 1)), sg.InputText('', key='identificador')],
            [sg.Text('Tipo do Investimento:', size=(15, 1)), sg.DropDown(['Renda Fixa', 'Renda Variável', 'Fundo Imobiliário'], key='tipo_investimento')],
            [sg.Text('Resumo do ativo:', size=(15, 1)), sg.InputText('', key='resumo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de ativo').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        valor_min = values['valor_min']
        identificador = values['identificador']
        tipo_investimento = values['tipo_investimento']
        resumo = values['resumo']

        for valor in values:
            if button == 'Cancelar':
                self.close()
                return 1
            if values[valor] == '':
                self.close()
                return False
        try:
            valor_min = int(valor_min)
        except ValueError:
            self.close()
            return 0

        self.close()
        return {"nome": nome, "valor_min": valor_min, "identificador": identificador, "tipo_investimento": tipo_investimento, "resumo":resumo}

    def print_mensagem(self, mensagem):
        sg.popup("", mensagem)