class MenorIdadeError(Exception):
    def __init__(self):
        self.mensagem = f"Usuário menor de idade não pode abrir conta"
        super().__init__(self.mensagem)