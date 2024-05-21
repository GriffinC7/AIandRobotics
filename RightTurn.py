from math import pi
from Robot373 import *
def RightTurn():
    def degrees(position):
        return position*1.0  # not sure of the conversion factor here -- is it 1?

    def distance_traveled(position):
        wheel_diameter_cm=8.5
        pi=3.141592653589793235
        
        return pi*wheel_diameter_cm*degrees(position)/360

        
    left,right=Motors("ab")

    left.power=20
    right.power=-25

    axis_length_cm=12
    distance_needed=(axis_length_cm/2)*2*pi/4  # need a quarter turn of the robot



    try:
        while distance_traveled(left.position)<distance_needed:
            print("distance traveled so far:",distance_traveled(left.position))
            Wait(0.01)
    except KeyboardInterrupt:
        pass
    
    left.power=0
    right.power=0
    
    return


    
    


