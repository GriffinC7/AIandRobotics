from Robot373 import *

from DistForward import distforward
from LeftTurn import leftturn
from PushPiece import backwards
from RightTurn import rightturn
left,right=Motors("ab")

#player=1  or player=2 depending on which you want
#state=read_state() # read the pieces, and construct the state
#move = # replace with minimax,skitles, Q, etc...
try:
    make_move =int(input('Choose a number 0 to 3: '))
    while make_move > 3 or make_move < 0:
        print('Not A valid Index')
        int(input('Choose a number 0 to 3:'))
    Wait(2)
    n=10
    if make_move==0:

        distforward(n)
        Wait(2.0)
        leftturn()
        Wait(0.34)
        distforward(n+7)
        Wait(2.0)
        backwards()
        Wait(1.0)
        rightturn()
        Wait(0.002)
        backwards()
        Wait(1.0)
    else:
        left.power=0
        right.power=0

except KeyboardInterrupt:
    pass  

Shutdown()






    