import payload
import digitalio
from board import *
from time import sleep
# Disable autoreload
import supervisor
supervisor.runtime.autoreload = False

# Vervollständige den Code um zu prüfen, ob der Angriff ausgeführt werden soll:
# attackMode = False
# attackPin = digitalio.DigitalInOut(???)
# attackPin.direction = digitalio.Direction.???
# attackPin.pull = digitalio.Pull.UP
# attackMode = attackPin.???

# Nutze die obige Variable um den Angriff nur unter bestimmten Bedingugen auszuführen:
# if(??? == True):
    # < --- Lasse die rote LED 10 mal blinken
    # Dabei soll sie 0.25 Sekunden an und wieder aus sein.
    #
    # --->
payload.run() # Nicht vergessen diese Zeile einzurücken.
# else:
    # < --- Lasse die grüne LED 10 mal blinken
    # Dabei soll sie 0.25 Sekunden an und wieder aus sein.
    #
    # --->
