import PySimpleGUI as sg


class TelaUsuario:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE USUARIO █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Listar Usuarios', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Cadastrar Usuario', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Alterar Usuario', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Remover Usuario', size=(25, 2), key='4', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Cancelar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de Usuários').Layout(layout)

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
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def mostra_usuario(self, dados_usuario):
        string_todos_usuarios = ""
        for usuario in dados_usuario:
            string_todos_usuarios = string_todos_usuarios + "NOME DO USUÁRIO: " + usuario["nome"] + '\n'
            string_todos_usuarios = string_todos_usuarios + "CPF DO USUÁRIO: " + str(usuario["cpf"]) + '\n'
            string_todos_usuarios = string_todos_usuarios + "DATA DE NASCIMENTO: " + usuario["data_nascimento"] + '\n'
            string_todos_usuarios = string_todos_usuarios + '\n'

        sg.Popup('░▒▓█ LISTA DE USUARIOS █▓▒░', string_todos_usuarios)

    def seleciona_por_cpf(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONAR USUARIO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o cpf do usuário que deseja selecionar: ', font=("Lucida", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona amigo').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()

        for valor in values:
            if button == 'Voltar':
                self.close()
                return 0
            if values[valor] == '':
                self.close()
                return False

        return int(cpf)

    def cadastrar_usuario(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ DADOS DO USUÁRIO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [
                sg.Text('Data de Nascimento:', size=(15, 1)),
                sg.InputCombo(list(range(1, 32)), key='dia_nascimento', default_value=1),
                sg.InputCombo(list(range(1, 13)), key='mes_nascimento', default_value=1),
                sg.InputCombo(list(range(1923, 2023)), key='ano_nascimento', default_value=2000)
            ],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de usuário').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        dia_nascimento = values['dia_nascimento']
        mes_nascimento = values['mes_nascimento']
        ano_nascimento = values['ano_nascimento']

        for valor in values:
            if button == 'Cancelar':
                self.close()
                return 1
            if values[valor] == '':
                self.close()
                return False
        try:
            cpf = int(cpf)
        except ValueError:
            self.close()
            return 0

        self.close()
        data_nascimento = str(f'{dia_nascimento}/{mes_nascimento}/{ano_nascimento}')
        return {"nome": nome, "cpf": cpf, "dia_nascimento": dia_nascimento,
                "mes_nascimento": mes_nascimento, "ano_nascimento": ano_nascimento,"data_nascimento":data_nascimento}

    def print_mensagem(self, mensagem):
        sg.popup("", mensagem)