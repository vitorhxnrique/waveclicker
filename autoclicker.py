import keyboard as key
from pynput.mouse import Button, Controller
import time

mouse = Controller()
clicking = False

def clicks(delay_entre_clicks):
    print("programa ativo, aperte f8 pra comecar a clicar/parar e 8 pra sair do programa")
    while True:
        global clicking
        if key.is_pressed("f8"):
            clicking = not clicking
            print("alternando entre click / not click")
            time.sleep(0.3)

        if key.is_pressed("8"):
            print("fechando programa")
            break
            

        if clicking == True:
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(delay_entre_clicks)


#delay_entre_clicks = float(input("qual o delay entre clicks desejado? (o menor e 0.1)\n"))


#clicks(delay_entre_clicks)
