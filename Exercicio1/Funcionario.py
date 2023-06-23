class Funcionario:
    def __init__(self,nome:str='',salario:float=0) -> None:
        self.__nome = nome
        self._salario = salario
    
    def addAumento(self,acrescimo) -> None:
        self._salario+=acrescimo
    
    def ganhoAnual(self,valor:float) -> float:
        pass

    def setSalario(self,valor:float=0.0)->float:
        self._salario = valor
    
    def exibeDados(self)->str:
        return f'Nome: {self.__nome} \n Salario: {self._salario}'