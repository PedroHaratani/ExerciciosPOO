from Cachorro import Cachorro
from Gato import Gato
from Rica import Rica
from Pobre import Pobre
from Miseravel import Miseravel

if __name__ == "__main__":
    ch = Cachorro('Rex')
    gt = Gato('Pititi')
    
    prc = Rica('Pedro',32,10000)
    ppb = Pobre('Adamastor',22)
    pml = Miseravel('José',50)


    print(ch.caminha())
    print(ch.latir())
    print(gt.caminha())
    print(gt.mia())
    print('////////////////////////////////////')
    print(prc.fazCompras())
    print(ppb.trabalha())
    print(pml.mendiga())