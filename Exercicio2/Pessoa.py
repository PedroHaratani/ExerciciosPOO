class Pessoa:
    def __init__(self,nome:str='',idade:float=0) -> None:
        self.__nome=nome
        self.__idade=idade

    def getNome(self):
        return self.__nome
    
