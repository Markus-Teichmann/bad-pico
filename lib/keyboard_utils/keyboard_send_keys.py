import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from keyboard_utils.keyboard_special_key_map import CTRLALTDEL
from keyboard_utils.keyboard_special_key_map import RUN
from keyboard_utils.keyboard_special_key_map import SPOTLIGHT
from keyboard_utils.keyboard_special_key_map import CLOSE

kbd = Keyboard(usb_hid.devices)

def send(keys, sleep=0.25): #Default Wert für sleep.
    # keys wird immer eine Liste sein, in der jeder key eine eigene Liste darstellt.
    # zum Beispiel sieht Test so aus: [[225, 23], [8], [22], [23]]
    # und CTRLALTDEL so: [[224, 226, 76]]
    for key in keys:
        kbd.press(*key)
        kbd.release_all()
    time.sleep(sleep)