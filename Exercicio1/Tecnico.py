from Assistente import Assistente
class Tecnico(Assistente):
    def __init__(self, nome: str = '', salario: float = 0, matricula: str = '') -> None:
        super().__init__(nome, salario, matricula)

    def ganhoAnual(self,valor:float) -> float:
        self.setSalario(self._salario+valor)
        return self._salario*12
         