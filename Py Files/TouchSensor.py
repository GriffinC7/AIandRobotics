from Robot373 import *
left,right=Motors("ab") 
touch=Sensors(None,'touch',None,None)

pressed=False

while True:
    if touch.value and not pressed:
        print("Button Pressed")
        pressed=True
    elif not touch.value and pressed:
        print("Button Released")
        pressed=False
        
        
        
Shutdown()