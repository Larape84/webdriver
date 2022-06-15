from datetime import date
import string
import pyautogui as robot
import time 
import pyperclip as clipboard
from pynput.keyboard import Key, Controller
import numpy as np
import pyautogui as pya
import pyperclip  
import mouse


keyboard = Controller()

time.sleep(5)

posicion=859,146

login="https://agenciapublicadeempleo.sena.edu.co/spe-web/spe/login"

consultar="https://agenciapublicadeempleo.sena.edu.co/spe-web/spe/funcionario/oferta"

userRegistrado="https://agenciapublicadeempleo.sena.edu.co/spe-web/spe/oferta/new"

cedula=[1082044112,1193544030]

nombres=['VÍCTOR JOSÉ','YIMMY JOSE']
apellido1=['LARA','OSPINO']
apellido2=['RADA','CARABALLO']
fechanacimiento=['12-06-2004','12-06-2004']
sexo=['f','f']

def copy_clipboard():
        pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
        pya.hotkey('ctrl', 'c')
        time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
        return pyperclip.paste()

click=1

def abrir():

    
    robot.press("tab",presses=14)
    robot.typewrite(str(cedula[1]))
    robot.press("enter",presses=1)
    time.sleep(3)
    robot.press("tab",presses=12)
    robot.press("enter",presses=1)
    time.sleep(5)
    pya.hotkey('f6')
        
    url=copy_clipboard()
    
    if (url!=userRegistrado and url!=consultar):
        robot.press("enter",presses=1)
        time.sleep(5)
        robot.press("tab",presses=3)
        robot.press("enter",presses=1)
        robot.press("tab",presses=1)
        robot.press("enter",presses=1)
    else:
        robot.moveTo(posicion)
        robot.click(clicks=click)
        robot.press("tab",presses=18)
        robot.typewrite(str(nombres[1]))
        time.sleep(1)
        robot.press("tab",presses=1)
        robot.typewrite(str(apellido1[1]))
        time.sleep(1)
        robot.press("tab",presses=1)
        robot.typewrite(str(apellido2[1]))
        time.sleep(1)
        robot.press("tab",presses=1)
        robot.press("enter",presses=1)

        if (sexo[1]=="m"):
            pya.hotkey('down')
            robot.press("enter",presses=1)
        if (sexo[1]=="f"):
            pya.hotkey('down')
            pya.hotkey('down')
            robot.press("enter",presses=1)

        def copiarFecha():
            pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
            pyperclip.copy(fechanacimiento[1])
            pya.hotkey('ctrl', 'c')
            time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
            return pyperclip.paste()
        
        copiarFecha()
        time.sleep(1)
        robot.press("tab",presses=1)
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)
        robot.press("enter",presses=1)
        robot.press("tab",presses=2)
        robot.press("enter",presses=1)
        time.sleep(1)
        robot.press("tab",presses=1)
        robot.press("enter",presses=1)   

        time.sleep(5)

        pya.hotkey('f6')
        url2=copy_clipboard()

        if("https://agenciapublicadeempleo.sena.edu.co/spe-web/spe/oferta/new"==url2):

            robot.moveTo(posicion)
            robot.click(clicks=click)

            robot.press("tab",presses=16)
            robot.press("enter",presses=1)
            robot.press("tab",presses=1)

            pya.hotkey('space') #Colombia
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)

            robot.press("enter",presses=1)

            time.sleep(2)
            robot.press("tab",presses=1)
            
            pya.hotkey('space') #atlantico
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)
        
            time.sleep(2)
            robot.press("tab",presses=1)

            #barranquilla
            pya.hotkey('space')
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)


            robot.press("tab",presses=5)
            robot.press("enter",presses=1)
            robot.press("tab",presses=1)


            pya.hotkey('space') #Colombia
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            robot.press("enter",presses=1)


            time.sleep(2)
            robot.press("tab",presses=1)
            
            pya.hotkey('space') #atlantico
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)


            time.sleep(2)
            robot.press("tab",presses=1)

            #barranquilla
            pya.hotkey('space')
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)

            robot.scroll(4)

            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)

            robot.press("enter",presses=1)
            pya.hotkey('down') #estadocivil
            robot.press("enter",presses=1)

            def copiarPersonas():
                pyperclip.copy("") 
                pyperclip.copy("2") # personas a cargo
                pya.hotkey('ctrl', 'c')
                time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                return pyperclip.paste()
                
            copiarPersonas()
            time.sleep(1)
            robot.press("tab",presses=1)
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl) #personas a cargo

            robot.press("tab",presses=1)

            pya.hotkey('down') #posicion familiar

            robot.press("tab",presses=1)

            pya.hotkey('down') #libreta
            robot.press("tab",presses=1)
            pya.hotkey('down') #no migrante
            robot.press("tab",presses=1)
            pya.hotkey('down') #urbana
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("tab",presses=1)
            time.sleep(0.3)
            robot.press("enter",presses=1)
            pya.hotkey('down') #salario
            time.sleep(0.3)
            pya.hotkey('down') #salario
            time.sleep(0.3)
            pya.hotkey('down') #salario
            time.sleep(0.3)
            robot.press("enter",presses=1)
            robot.press("tab",presses=1)

            pya.hotkey('space') #Colombia
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            pya.hotkey('c',presses=1)
            time.sleep(0.1)
            robot.press("enter",presses=1)
            time.sleep(2)

            robot.press("tab",presses=1)
            pya.hotkey('space') #atlantico
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)
            time.sleep(2)

            robot.press("tab",presses=1)
            #barranquilla
            pya.hotkey('space')
            pya.hotkey('down')
            time.sleep(0.1)
            pya.hotkey('down')
            time.sleep(0.1)
            robot.press("enter",presses=1)

            robot.press("tab",presses=3)
            robot.typewrite("BARRANQUILLA")# DIRECCION
            time.sleep(0.3)

            robot.press("tab",presses=3)
            pya.hotkey('down')

            robot.press("tab",presses=1)
            robot.typewrite("3155497360")# TELEFONO
            time.sleep(0.3)
            robot.press("tab",presses=8)
            robot.typewrite("LJARAPEMISENA.EDU.CO")# CORREO

            robot.press("tab",presses=1)
            robot.typewrite("BACHILLER")# PROFESION
            time.sleep(1)
            robot.press("tab",presses=2)
            robot.press("enter",presses=1)






abrir()                                                                                                