import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from keyboard_utils.keyboard_special_key_map import CTRLALTDEL
from keyboard_utils.keyboard_special_key_map import RUN
from keyboard_utils.keyboard_special_key_map import SPOTLIGHT
from keyboard_utils.keyboard_special_key_map import CLOSE

kbd = Keyboard(usb_hid.devices)

def send(this_input, sleep=0.25): #Default Wert für sleep.
    if type(this_input) is list:
	if this_input in [CTRLALTDEL, RUN, SPOTLIGHT, CLOSE]:
	    for item in this_input:
	        if type(item) is list:
		    kbd.press(*item)
		else:
		    kbd.press(item)
	    kbd.release_all()
	else:
            for item in this_input:
                if type(item) is list: #Prüft, ob item eine Liste ist.
                    kbd.send(*item)
                else:
                    kbd.send(item)
    else:
        kbd.send(this_input)
    time.sleep(sleep)