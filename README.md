# bad-pico
Ausführen von HID-Angriffen im Rahmen eines Schulprojekts mit einem Raspberry-Pi Pico, CircuitPython, Adafruit_HID und thonny. Dieses Projekt wird sich auf einen Raspberry Pico W beschränken, der Code könnte aber auch auf einem Pico funktionieren.

## Einrichten

### Aktuelle Version

### Neuere Versionen
 - Circuit-Python: https://circuitpython.org/board/raspberry_pi_pico_w/ 
 - Adafruit-HID: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

## Code Ausführen
Jede Payload.py Datei muss eine Methode run definieren. Diese wird in code.py importiert und dort beim Start ausgeführt.
## Reset
Sollte etwas schief gehen, so beim nächsten Anschließen den BootSel Knopf gedrückt halten. Danach die sich in reset/ befindende UT2 Datei auf den Pico ziehen und alles neu einrichten. Achtung hier gehen Daten verloren.
## Quellen
Thonny: https://github.com/thonny/thonny/releases

Inspiration für dieses Projekt:
- pico-ducky: https://github.com/dbisu/pico-ducky
- pico-hid: https://github.com/treguly/pico-hid
- Austin's lab: https://www.youtube.com/watch?v=ctCmOhoT9po
- John Gallaugher: https://www.youtube.com/watch?v=fTeiPwYLw8w

