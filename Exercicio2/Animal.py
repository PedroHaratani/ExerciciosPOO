class Animal:
    def __init__(self) -> None:
        self.__nome=""
        self.__raca=""
    
    def __init__(self,nome:str='') -> None:
        self.__nome=nome

    def caminha(self)->str:
        return f'{self.__nome} caminhando'