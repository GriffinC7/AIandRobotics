from Robot373 import *

left,right=Motors("ab")


left.power=20
right.power=40

Wait(5)

left.power=40
right.power=20

Wait(5)

left.power=0
right.power=0

Wait(5)



Shutdown()
