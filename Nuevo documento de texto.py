import pyautogui as robot
import time 
import pyperclip as clipboard


apen=508,1061

def abrir(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

abrir(apen,click=2)
