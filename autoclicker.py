import keyboard as key
from pynput.mouse import Button, Controller
import time

mouse = Controller()
clicking = False

while True:
    if key.is_pressed("f8"):
        clicking = True
        print("Clicking iniciado")
        time.sleep(0.3)

    if key.is_pressed("8"):
        clicking = False
        print("Clicking parado")
        time.sleep(0.3)

    if clicking:
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.1)
