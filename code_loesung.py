import payload
import digitalio
from board import *
from time import sleep
# Disable autoreload
import supervisor
supervisor.runtime.autoreload = False

attackPin = digitalio.DigitalInOut(GP15)
attackPin.direction = digitalio.Direction.INPUT
attackPin.pull = digitalio.Pull.UP
attackMode = attackPin.value

if(attackMode == True):
    red_led = digitalio.DigitalInOut(GP10)
    red_led.direction = digitalio.Direction.OUTPUT
    for i in range(0,10):
        red_led.value = True
        sleep(0.25)
        red_led.value = False
        sleep(0.25)
    payload.run()
else:
    green_led = digitalio.DigitalInOut(GP21)
    green_led.direction = digitalio.Direction.OUTPUT
    for i in range(0,10):
        green_led.value = True
        sleep(0.25)
        green_led.value = False
        sleep(0.25)
