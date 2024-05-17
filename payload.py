from keyboard_utils.keyboard_fkeys_map import *
from keyboard_utils.keyboard_special_key_map import *
from keyboard_utils.keyboard_character_map import get_code
from keyboard_utils.keyboard_send_keys import send
from time import sleep

def repeat():
    for i in range(0,3):
        send(get_code(i))
        send(ENTER)

def run():
    sleep(5)
    send(CLOSE, 1)
    send(RUN, 1)
    send(get_code('notepad'), 1)
    send(ENTER, 2)
    send(get_code('Hallo Welt!'))
    send(ENTER)
    repeat()
    
#run()