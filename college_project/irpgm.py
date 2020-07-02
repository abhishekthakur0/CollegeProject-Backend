import RPi.GPIO as IO
import time
from fbdata import syncWithCloud

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input


while 1:
    if True:
        if(IO.input(14)==False): #object is far away
            IO.output(2,True) #Red led ON
            IO.output(3,False) # Green led OFF
            print(IO.input(14))

        if(IO.input(14)==True): #object is near
            IO.output(3,True) #Green led ON
            IO.output(2,False) # Red led OFF
            print(IO.input(14))