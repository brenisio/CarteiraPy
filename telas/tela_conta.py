import PySimpleGUI as sg


class TelaConta:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ LOGIN █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Cadastro', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Login', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Contas cadastradas', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Cancelar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de contas').Layout(layout)

    def primeira_tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def login_init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CARTEIRA DO PY █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Consultar Saldo', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Depositar', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Sacar', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Mostrar ativos disponíveis', size=(25, 2), key='4', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Comprar ativo', size=(25, 2), key='5', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Vender ativo', size=(25, 2), key='6', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Mostrar seus ativos', size=(25, 2), key='7', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Consultar suas ordens', size=(25, 2), key='8', button_color=('white', 'black'),
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

    def segunda_tela_opcoes(self):
        self.login_init_opcoes()
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
        if button == '5':
            opcao = 5
        if button == '6':
            opcao = 6
        if button == '7':
            opcao = 7
        if button == '8':
            opcao = 8
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao


    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_ativos_conta(self, dados_ativo):
        string_todos_ativos = ""
        for ativo in dados_ativo:
            string_todos_ativos = string_todos_ativos + "NOME DO ATIVO: " + ativo["nome"] + '\n'
            string_todos_ativos = string_todos_ativos + "VALOR MINIMO DO ATIVO: " + ativo["valor_min"] + '\n'
            string_todos_ativos = string_todos_ativos + "IDENTIFICADOR: " + ativo["identificador"] + '\n'
            string_todos_ativos = string_todos_ativos + "TIPO DO INVESTIMENTO: " + ativo["tipo_investimento"] + '\n'
            string_todos_ativos = string_todos_ativos + "RESUMO INVESTIMENTO: " + ativo["resumo"] + '\n'
            string_todos_ativos = string_todos_ativos + '\n'

        sg.Popup('░▒▓█ LISTA DE ATIVOS █▓▒░', string_todos_ativos)

    def seleciona_por_id_conta(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONAR A CONTA POR ID █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o id da conta:', font=("Lucida", 15))],
            [sg.Text('id_conta:', size=(15, 1)), sg.InputText('', key='id_conta')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona conta').Layout(layout)

        button, values = self.open()
        id_conta = values['id_conta']
        self.close()
        return id_conta

    def fazer_login(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ FAÇA O LOGIN █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o id da conta:', font=("Lucida", 15))],
            [sg.Text('id_conta:', size=(15, 1)), sg.InputText('', key='id_conta')],
            [sg.Text('Digite a senha:', font=("Lucida", 15))],
            [sg.Text('senha:', size=(15, 1)), sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona conta').Layout(layout)

        button, values = self.open()
        id_conta = values['id_conta']
        senha = values['senha']
        self.close()
        return id_conta, senha

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
        if button == 'Voltar':
            self.close()
            return 'Voltar'
        try:
            return int(cpf)
        except:
            return False

    def insere_identificador_ativo(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONE O IDENTIFICADOR DO ATIVO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o identificador do ativo:', font=("Lucida", 15))],
            [sg.Text('identificador:', size=(15, 1)), sg.InputText('', key='identificador')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona valor').Layout(layout)

        button, values = self.open()
        if button == 'Voltar':
            self.close()
            return 1
        identificador = values['identificador']
        self.close()
        return identificador

    def insere_valor(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('-------- ░▒▓█ SELECIONE A QUANTIA R$ █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text('Digite o valor desejado:', font=("Lucida", 15))],
            [sg.Text('valor:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona valor').Layout(layout)

        button, values = self.open()
        if button == 'Voltar':
            self.close()
            return 0

        valor = values['valor']
        try:
            self.close()
            return int(valor)
        except:
            self.close()
            return False

    def mostra_conta(self, dados_conta):
        string_todas_contas = ""
        for conta in dados_conta:
            string_todas_contas = string_todas_contas + "NOME USUÁRIO: " + conta["nome"] + '\n'
            string_todas_contas = string_todas_contas + "CPF: " + str(conta["cpf"]) + '\n'
            string_todas_contas = string_todas_contas + "ID LOGIN: " + conta["id_conta"] + '\n'
            string_todas_contas = string_todas_contas + "TIPO DE PERFIL: " + conta["tipo_perfil"] + '\n'
            string_todas_contas = string_todas_contas + "SALDO: " + str(conta["saldo"]) +'R$ '+'\n'
            string_todas_contas = string_todas_contas + '\n'

        sg.Popup('░▒▓█ LISTA DE CONTAS █▓▒░', string_todas_contas)

    def identificar_perfil_investidor(self):
        lista_respostas = []
        possiveis_respostas = [1, 2, 3]
        perguntas = 1
        perfil_investidor = None

        dict_perguntas = {
            1: "Qual o seu principal objetivo ao investir seu dinheiro?\n\n\
    1: Preservar meu patrimônio assumindo um menor risco\n\
    2: Uma combinação entre preservação do patrimônio e sua valorização\n\
    3: Maximizar o potencial de ganho assumindo um maior risco",

            2: "Quanto você está disposto a investir?\n\n\
    1: De 0 a R$ 10000\n\
    2: De R$ 10000 a R$ 25000\n\
    3: Acima de R$ 25000",

            3: "Qual é a sua necessidade em relação ao dinheiro que está investindo?\n\n\
    1: Preciso deste dinheiro como complemento de renda\n\
    2: Eventualmente posso precisar utilizar uma parte dele\n\
    3: Não tenho necessidade imediata deste dinheiro",

            4: "Por conta de oscilações do mercado, considere que seus investimentos percam 10%/ do valor aplicado. Neste caso, o que você faria?\n\n\
    1: Tiraria todo o dinheiro\n\
    2: Manteria o dinheiro\n\
    3: Colocaria mais dinheiro",

            5: "Considerando sua formação, é possível afirmar que:\n\n\
    1: Não possuo formação relacionada ao mercado financeiro\n\
    2: Minha formação está substancialmente relacionada ao mercado financeiro\n \
    3: Minha formação está diretamente relacionada ao mercado financeiro",

            6: "Considerando sua experiência profissional, é possível afirmar que:\n\n\
    1: Não possuo experiência sobre mercado financeiro\n\
    2: Minha experiência em mercado financeiro é razoável e algumas vezes preciso de orientação profissional \n\
    3: Tenho vasto conhecimento em mercado financeiro e me sinto seguro ao investir sem orientação profissional ",

            7: "Como você descreveria sua expectativa de renda futura para os próximos 5 anos?\n\n\
    1: Minha renda deve diminuir devido à aposentadoria, mudança de emprego, diminuição de faturamento, etc\n \
    2: Minha renda deve se manter estável \n\
    3: Minha renda deve aumentar devido a uma promoção, novo emprego, aumento de faturamento, etc\n"
        }

        layout = [
            [sg.Text('-------- ░▒▓█ DADOS DO USUÁRIO █▓▒░ ----------', font=("Lucida", 25))],
            [sg.Text(dict_perguntas[perguntas], key='-PERGUNTA-')],
            [sg.InputCombo(possiveis_respostas, key='resposta')],
            [sg.Button('Próxima pergunta'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Perfil de Investidor', layout)

        while True:
            button, values = window.read()
            if button == 'Cancelar':
                window.close()
                return 1

            if values['resposta'] == '':
                sg.Popup('Você não selecionou um número')
                continue

            p1 = int(values['resposta'])
            if p1 in possiveis_respostas:
                lista_respostas.append(p1)
            else:
                window.close()
                return False

            perguntas += 1

            if perguntas > 7:
                break

            window['-PERGUNTA-'].update(dict_perguntas[perguntas])
            window['resposta'].update(value='')

        window.close()

        qtd_1 = lista_respostas.count(1)
        qtd_2 = lista_respostas.count(2)
        qtd_3 = lista_respostas.count(3)

        if qtd_2 < qtd_1 > qtd_3 or qtd_1 == qtd_2 or qtd_1 == qtd_3:
            perfil_investidor = 'Conservador'
        elif qtd_1 < qtd_2 > qtd_3 or qtd_2 == qtd_3:
            perfil_investidor = 'Moderado'
        elif qtd_1 < qtd_3 > qtd_2:
            perfil_investidor = 'Arrojado'

        return perfil_investidor

    def print_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def cadastrar_senha(self):
        layout = [
            [sg.Text("Digite sua senha (6 números):")],
            [sg.Input(key="-SENHA1-")],
            [sg.Text("Confirme sua senha:")],
            [sg.Input(key="-SENHA2-")],
            [sg.Button("Cadastrar")]
        ]

        window = sg.Window("Cadastro de Senha", layout)

        for tentativas in range(3):
            event, values = window.read()
            senha1 = values["-SENHA1-"]
            senha2 = values["-SENHA2-"]

            if len(senha1) != 6 or not senha1.isdigit():
                sg.popup("A senha deve conter exatamente 6 números.")
            elif senha1 != senha2:
                sg.popup("As senhas não coincidem. Tente novamente")
            else:
                senha = {"senha": senha1}
                window.close()
                return senha

        sg.popup("O número de tentativas foi excedida.")
        window.close()
        return False