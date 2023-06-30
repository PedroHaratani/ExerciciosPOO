from Animal import Animal
class Cachorro(Animal):
    def __init__(self, nome: str = '') -> None:
        super().__init__(nome)
    
    def latir(self)->str:
        return f'Au Au Au!'