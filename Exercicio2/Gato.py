from Animal import Animal

class Gato(Animal):
    def __init__(self, nome: str = '') -> None:
        super().__init__(nome)
    
    def mia(self)->str:
        return f'Miau!'