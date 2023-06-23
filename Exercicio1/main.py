from Administrativo import Administrativo
from Tecnico import Tecnico

if __name__ == "__main__":
    ad = Administrativo('Raul',3000,'r4325')
    tc = Tecnico('Guilherme',2500,'g5678')

    ad.ganhoAnual(500)
    tc.ganhoAnual(700)

    print(f'{ad.exibeDados()} \n')
    print(f'{tc.exibeDados()} \n')