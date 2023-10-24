class ListaVaziaError(Exception):
    def __init__(self,msg=''):
        if msg == '':
            self.mensagem =f"A lista está vazia."
        else:
            self.mensagem = f"A lista está vazia. {str(msg)}"
        super().__init__(self.mensagem)