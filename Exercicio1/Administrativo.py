from Assistente import Assistente

class Administrativo(Assistente):
    def __init__(self, nome: str = '', salario: float = 0, matricula: str = '') -> None:
        super().__init__(nome, salario, matricula)
    
    def ganhoAnual(self,valor:float) -> float:
        salario = self._salario
        self.setSalario(self._salario+valor)
        return self._salario*12
        