import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        # cover the cases of going back, not clicking anything, closing the window, or clicking cancel
        if button == '0' in (None, 'Cancelar'):
            opcao = 0
        print(opcao)
        self.close()
        return opcao

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('Bem vindo ao Carteira do Py!', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Usuário', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Ativo', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Acesse a conta', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Finalizar sistema', size=(25, 2), key='0', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Cancelar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'  # Centraliza os elementos dentro da coluna
            )]
        ]
        self.__window = sg.Window('Carteira de Investimentos').Layout(layout)