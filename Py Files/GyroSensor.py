from Robot373 import *

gyro_sensor=Sensors('gyro',None,None,None)

try:
    while True:
        gyro=gyro_sensor.value
        print(gyro)
        Wait(0.05)
except KeyboardInterrupt:
    pass



Shutdown()