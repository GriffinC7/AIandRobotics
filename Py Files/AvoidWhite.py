from cmath import pi
from Robot373 import *
from RightTurn import *

left,right=Motors("ab")

color_sensor=Sensors("color",None,None,None)
print("Waiting for sensor to warm up...")
while color_sensor.value is None:
    Wait(0.05)
print("done.")



try:
    while True:

         r,g,b,something=color_sensor.value
         print(r,g,b,something)
         print(closest_color(r,g,b,
                white=[256,256,256],
                black=[0,0,0],
                ))
        
         Wait(0.05)
        
         if closest_color(r,g,b,
                white=[256,256,256],
                black=[0,0,0],
                ) == 'black':
            left.power=20
            right.power=20
            
         elif closest_color(r,g,b,
                white=[256,256,256],
                black=[0,0,0],
                )=='white':
            
            RightTurn()

            left.power=20
            right.power=20

            Wait(0.01)
except KeyboardInterrupt:
    pass
Shutdown()