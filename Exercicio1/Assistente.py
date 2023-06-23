from Funcionario import Funcionario

class Assistente(Funcionario):
    def __init__(self, nome: str = '', salario: float = 0, matricula: str = '') -> None:
        self.__matricula = matricula
        super().__init__(nome, salario)

    def setMatricula(self,matricul) -> None:
        self.__matricula = matricul
    
    def getMatricula(self) -> str:
        return self.__matricula
    
    def exibeDados(self) -> str:
        return f'{super().exibeDados()} \n matricula: {self.__matricula}'
