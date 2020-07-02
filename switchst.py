import RPi.GPIO as GPIO
import time

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings
GPIO.setwarnings(False)
pins = [2,3,4,17]

GPIO.setup(pins, GPIO.OUT)



print("Enter Your Choice of Color")
print("1.Red\n2.Green\n3.Blue")
n = int(input())



if n==1:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(5)
    GPIO.cleanup()

if n==2:
    GPIO.output(3,GPIO.HIGH)
    time.sleep(5)
    GPIO.cleanup()

if n==3:
    GPIO.output(4,GPIO.HIGH)
    time.sleep(5)
    GPIO.cleanup()

if n==4:
    GPIO.output(17,GPIO.HIGH)
    time.sleep(5)
    GPIO.cleanup()
