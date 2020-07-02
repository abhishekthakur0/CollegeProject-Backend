# Write your code here :-)
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while True:
    i = GPIO.input(11)
    if i==0:
        print("No Object",i)
        GPIO.output(3,0)
        #time.sleep(2.1)
    elif i ==1:
        print("Object",i)
        GPIO.output(3,1)
        #time.sleep(2.1)