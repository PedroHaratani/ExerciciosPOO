from Pessoa import Pessoa

class Miseravel(Pessoa):
    def __init__(self, nome: str = '', idade: float = 0) -> None:
        super().__init__(nome, idade)
    
    def mendiga(self)->str:
        return f'{self.getNome()} mendiga'