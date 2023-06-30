from Pessoa import Pessoa

class Rica(Pessoa):
    def __init__(self, nome: str = '', idade: float = 0,dinheiro:float=0) -> None:
        super().__init__(nome, idade)
        self.__dinheiro=dinheiro
    
    def fazCompras(self)->None:
        return f'{self.getNome()} faz compras'
    

