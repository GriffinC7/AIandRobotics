from Robot373 import *

ultrasonic_sensor = Sensors(None,None,"us",None)
a,b = left,right=Motors("ab")

try:
    while True:
        eyes=ultrasonic_sensor.value
        print(eyes)
        Wait(0.05)
        if eyes <= 10.0:
            left.power=25
            right.power=25
        else:
            left.power=0
            right.power=0
except KeyboardInterrupt:
    pass


    
Shutdown()
        
        