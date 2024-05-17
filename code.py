from payload import run
import digitalio
from board import *
from time import sleep
# Disable autoreload
import supervisor
#supervisor.disable_autoreload()
supervisor.runtime.autoreload = False

attackMode = False
attackPin = digitalio.DigitalInOut(GP15) #Der Pin 15 wird zu einem Input oder Output Pin
attackPin.direction = digitalio.Direction.INPUT #Der Pin wird ein Input Pin
attackPin.pull = digitalio.Pull.UP #Wenn an diesem Pin kein Input anliegt, können wir hier so Strom anlegen, sodass wir true lesen.
attackMode = attackPin.value #Der Digitale Wert des Pins wird ausgelesen

if(attackMode == True):
    print("attackMode == True")
    red_led = digitalio.DigitalInOut(GP10)
    red_led.direction = digitalio.Direction.OUTPUT
    red_led.value = True
    run()
    for i in range(0,10):
        red_led.value = False
        sleep(0.25)
        red_led.value = True
        sleep(0.25)
    red_led.value = False
else:
    print("attackMode == False")
    green_led = digitalio.DigitalInOut(GP21)
    green_led.direction = digitalio.Direction.OUTPUT
    for i in range(0,10):
        green_led.value = True
        sleep(0.25)
        green_led.value = False
        sleep(0.25)
    green_led.value = True
