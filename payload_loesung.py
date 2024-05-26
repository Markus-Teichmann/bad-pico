from keyboard_utils.keyboard_fkeys_map import *
from keyboard_utils.keyboard_special_key_map import *
from keyboard_utils.keyboard_character_map import get_code
from keyboard_utils.keyboard_send_keys import send
from time import sleep

def run():
    sleep(2)
    send(CLOSE, 1)
    send(RUN, 1)
    send(get_code('notepad'), 1)
    send(ENTER, 1)
    send(get_code('Hallo Welt!'))

#run()
