from Robot373 import *

from DistForward import distforward
left,right,arm=Motors("abc")

#pickup()

def backwards():
    left.power=-10
    right.power=-10
    Wait(1.5)

    left.power=0
    right.power=0
    Wait(0.05)
    
distforward(15)   
backwards()
Shutdown()