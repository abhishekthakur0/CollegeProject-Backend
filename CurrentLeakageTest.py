from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)
intense = 0.1
while intense<1.0:
    led.value = intense
    sleep(1)
    intense = intense+0.1

led.close()