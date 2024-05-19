from keyboard_utils.keyboard_fkeys_map import *
from keyboard_utils.keyboard_special_key_map import *
from keyboard_utils.keyboard_character_map import get_code
from keyboard_utils.keyboard_send_keys import send
from time import sleep

def run():
    print("running Payload")
    # <--- Payload:
    # Schreibe hier einen Code, der durch die emulation von
    # Tastatureingaben den Editor "notepad" öffnet und in
    # diesen den String "Hallo Welt" schreibt.
    #
    # Verwende dabei die Befehle:
    
    # sleep(x)
        # lässt den Computer für x Sekunden schlafen bzw. nichts tun.
        
    # get_code('x')
        # liefert einen für den Computer verständlichen Code zu den Tasten x zurück.
        # Zum Beispiel liefert get_code('Test') die Liste: [[225, 23], [8], [22], [23]]
        
    # send(x, y)
        # sendet den Code für die Tasten x an den Computer und schläft dann y Sekunden
        # y ist hier nur optional
    
    # Tipp: Ein Auflistung aller spezieller Tasten wie zum Beispiel: ENTER
    # findest du auf dem Arbeitsblatt
    # --->
#run()