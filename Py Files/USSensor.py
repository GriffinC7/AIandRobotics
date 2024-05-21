from Robot373 import *

left,right=Motors("ab")

ultrasonic_sensor=Sensors(None,None,'us',None)
print("Waiting for sensor to warm up...")
while ultrasonic_sensor.value is None:
    Wait(0.05)
print("done.")

try:
    while True:
        eyes=ultrasonic_sensor.value
        print(eyes)
        Wait(0.05)
        if eyes<10 or eyes>200: # turn right
            left.power=10
            right.power=-10
            print('Turning Right')
            
        elif eyes>18: # turn left
            left.power=-10
            right.power=10
            print('Turning Left')
        else:  # go forward
            left.power=10
            right.power=10
       # if eyes <= 7.0 or eyes >= 150.0:
           # left.power=10
           # right.power=-10
           # print('WALL')
           # Wait()
        
            
       # else:
           # left.power=10
          #  right.power=10
except KeyboardInterrupt:
    pass


    
Shutdown()
        
        