from Pessoa import Pessoa

class Pobre(Pessoa):
    def __init__(self, nome: str = '', idade: float = 0) -> None:
        super().__init__(nome, idade)

    def trabalha(self)->str:
        return f'{self.getNome()} trabalha'