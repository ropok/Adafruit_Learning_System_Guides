# CircuitPython IO demo #1 - General Purpose I/O

import time
from digitalio import DigitalInOut, Direction, Pull
import board

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.D2)  # For Gemma M0, Trinket M0, Metro M0 Express, ItsyBitsy M0 Express
# switch = DigitalInOut(board.D5)  # For Feather M0 Express
# switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP


while True:
    # We could also just do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
