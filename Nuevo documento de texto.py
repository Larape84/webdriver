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

cedula=[1043691654,1044601693,1048292987,1002133737,1002480579,1143158251,1002163328,1001886029,1074344712,1193527339,1065580018,1143441095,1051357666,1044609037,8800506,1043124728,1081907378,1007236562,1044614546,1005469401,1004122585,1002344675,1043846106,1004281312,1129507009,1002227942,1007435984,1081907379,1007205235,1001780483,1007226762,1080434023,1100622309,1130266240,1004271082,18880943,1001939634,72298447,1043439521,1082570383,1052069970,1128200305,1193544548,1047036936,1004212747,1143269154,1134244037,1000941335,1002442529,1007564004,1193328272,1129531672,1051734253,1128165119,1128106644,1080010249,1052544096,1052947447,1010139109,1004279718,1002162782,1001946142,1002441695,1043159001,1006817007,1080540274,1066083746,1002028440,1002463130,1007964074,1002134266,1003166182,1081758353,1007956982,1043118051,1043123798,1081758368,1004119774,1043116207,1083433454,1001915810,1082044262,1129489149,1103094222,1102576379,1079654834,1080540148,1143115618,1103095411,1003191253,1002442529,1101382655,1082044022,1007116125]
nombres=['LUIS CARLOS','YESIDID','ANDRES FELIPE','MARLON MIGUEL','JORGE LUIS','JUAN DIEGO','ANDRES FELIPE','DANIEL','EMIRO RAFAEL','JHONATAN JAVIER','JOSIMAR','CARLOS MARIO','MOISES DAVID','MIGUEL SEGUNDO','CARLOS MARIO','DEIVIS JOSE','LUIS MIGUEL','RICARDO JOSE','MANUEL DE JESUS','KEINER ANDRES','JULIO CESAR','FRANCISCO JAVIER','JUAN DANIEL','STEFANIA','JESUS DANIEL','JESUS DAVID','HERASMO RAFAEL','KEINER MANUEL','SHIRLEYS PAOLA','ARMANDO FELIX','ANA','JUAN ESTEBAN','BRAYAN MANUEL','YELITZA PAOLA','JINHO DALBERTO','JOSE GREGORIO','KARL LEWIS DE JESUS','KEYNER','SHAIRA PAOLA','JESUS DAVID','CLOVIS MORAIMA','MIGUEL ANGEL','ANDRES FELIPE','YOLEINER DE JESUS','DANIS','ANDRES MODESTO','SERGIO ANDRES','CARLOS ADOLFO','BRAYAN ELIAS','DEISY DEL CARMEN','CAROLAY PATRICIA','NORMA','YESID ALEJANDRO','ISSA KATHERIN','MARISOL','SUREY PATRICIA','JORGE ANDRES','ROTHSAMBI','MOISES DAVID','HELEN MARGARITA','ROSMARIS','ANGIE PAOLA','ARIANA','MARIA PAZ','JENNIFER DEL AMPARO','MARLON SANTIAGO','ANA GABRIELA','JOSE DANIEL','JHON HECTOR','JORGE DANIEL','YENNIS CAMILA','JOSE CARLOS','MELANI MELISSA','JOSMIN ADRIAN','SHARID DANIELA','MARIA ANGELICA','LAURA VANESSA','NAYELIS MELISA','MARIA JOSE','CAMILO ANDRES','MARLEIDIS JOSE','ANDRU JOSE','KATIANA','LUISA ELENA','JOAQUIN JOSE','EDUAR DAVID','KATERINE LAUDID','MARIA ANGELICA','MARIA CAMILA','CARLOS ADOLFO','VIERIS MARIA','YERINEL PATRICIA','GLEYDIS MILENA']
apellido1=['OLIVERA','HERNANDEZ','ESPINOSA','GOMEZ','TOVAR','SANABRIA','SANTIAGO','RIBON','ROMERO','BALLESTA','MORRON','ORTIZ','TORRES','CAUSIL','BELTRAN','RODRIGUEZ','GUTIERREZ','PEREA','HENRÍQUEZ','POLO','VARGAS','BARRAZA','GARCIA','ROMERO','POLO','CARO','RODRIGUEZ','NAVARRO','BALZA','MEZA','ISABEL','DOMINGUEZ','DIAZ','MARTINEZ','DIAZ','CARO','DELGADO','ARTEAGA','VERGARA','MORA','OJEDA','CALDERIN','BURGOS','SILVA','VANEGAS','FONTALVO','ANAYA','VEGA','ROSALES','ESCORCIA','RESTREPO','CHICA','GASTELBONDO','PERTUZ','CONRADO','CHAMORRO','LOPEZ','RIOS','BUELVAS','ROMERO','BENITEZ','ESTRADA','ARIAS','NUÑEZ','FONTALVO','NIETO','CABARCAS','CARO','PEREZ','ACEVEDO','GONZALEZ','DE LA CRUZ','BRAVO','MORENO','ACOSTA','SALAS','ALMANZA','VARGAS','JIMENEZ','VARGAS','GUTIERREZ','MUÑOZ','VERGARA','LARA','CARO','CAMARGO','CASTRILLON','GUERRA','VASQUEZ','VEGA','VALDES','CHARRIS','ZARATE']
apellido2=['MORENO','PEREZ','AGUDELO','MACIAS','NOVOA','DIAZ','OLIVERA','OSORIO','BROCHERO','ALTAMIRANDA','ARENAS','COLON','RODRIGUEZ','GALVIS','BALTAZAR','CHACON','BOCANEGRA','PADILLA','ROMERO','ORTIZ','ACOSTA','CERPA','MELENDEZ','GUTIERREZ','GUERRA','SOTO','CHACON','MARQUEZ','VILLAR','OJITO','MERCADO PACHECO','CARMONA','MORELO','FANDIÑO','TEHERAN','ACOSTA','RADA','SANCHEZ','VARGAS','VEGA','BANQUEZ','MEDINA','ANGULO','RODRIGUEZ','PEREZ','CERVANTES','PACHECO','TORRES','ACOSTA','CERPA','PABON','VILLALBA','OSORIO','OLAYA','BORJA','DE LA CRUZ','BONILLA','PUELLO','TORRES','RIVERA','MARTINEZ','NAVARRO','MERCADO','PRADO','OLAYA','MEJIA','TORREGROSA','BARCAS','YANCE','ALCALA','TRUJILLO','DOMINGUEZ','POSADA','PEREZ','CAMARILLO','CARBONELL','FIGUEROA','MUÑOZ','AGUILAR','GERRERO','FERREIRA','GIRALDO','GUARIN','NAVARRO','DAVILA','CAMACHO','PEÑA','CERMEÑO','ATENCIO','TORRES','SALAZAR','VARGAS','DE LA HOZ']
fechanacimiento=['12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004','12-06-2004']
sexo=['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m']
correo=['luiscaolivera2020@gmail.com','yesidhernandez919@gmail.com','espinosandres095@gmail.com','dametucuenta08@gmail.com','stiventovar63@gmail.com','amaurighisays@hotmail.com','andreselfrente@gmail.com','esteban20052915@gmail.com','emirorafaelromerobrochero@gmail.com','jhonatanballesta17@gmail.com','josimarmorron@gmail.com','co716802@gmail.com','danielatorresr28@gmail.com','causilmiguelsegundox3@gmail.com','cb1229207@gmail.com','rdz06darell@gmail.com','gutierrezpertuzl@gmail.com','ricardoperea92@hotmail.com','manuelhenriquezromero14@gmail.com','keinerandrespoloortiz@gmail.com','juliocesarvargas199924@gmail.com','Francisco_barraza@hotmail.es','espitiadairany@gmail.com','romerogutierrezsthefania@gmail.com','Jesusdanielpologuerra@gmail.com','jesusdavidcaro10@gmail.com','herasmorodriguez160@gmail.com','keinernavarromarquez@gmail.com','yeinerguerrero02@gmail.com','armando19meza@gmail.com','anaisabelmercadopacheco@gmail.com','dominguezcarmonayulieth@gmail.com','Bdiazmorelos2001@hotmail.com','martinezfandinoyelitza@gmail.com','jinhodiaz25@gmail.com','margaruiz_19@hotmail.com','lewis1985@hotmail.es','keiner07manco@gmail.com','shairavergara99@gmail.com','moravegaj7@gmail.com','ojedabanquezclovis@gmail.com','miguelcalderin17@gmail.com','pipeburgos15@gmail.com','dejesussilva1212@gmail.com','danisvanegas18@gmail.com','fontalvoandresmc@gmail.com','sergiioandres1101@gmail.com','0412vega.c@gmail.com','brayanrosales279@gmail.com','deisyescorcia1999@gmail.com','Carolayr363@gmail.com','nchicavillalba@gmail.com','yesidgastelbondo12@gmail.com','malejapv17@gmail.com','marisolconrado1999@gmail.com','sureychamorro@gmail.com','jorgeandreslopezbonilla@gmail.com','rosaney025@gmail.com','moisesmdbt@gmail.com','ROMERORIVERAHELEN@GMAIL.COM','benitezmartinezrosmaris@gmail.com','angieestrada.3099@gmail.com','sabriu2@gmail.com','mnunezprado0@gmail.com','fontalvoolayayenifer@gmail.com','nietomarlon661@gmail.com','cabarcas_ana07@yahoo.com','carobarcasj@gmail.com','jhonhector.y@outlook.com','da1471633@gmail.com','camilagonzalestrujillo12@gmail.com','jd982266@gmail.com','melanibravo520@gmail.com','josminadrian@gmail.com','acostasharid25@gmail.com','mariaangelicasalas780@gmail.com','ivafigueroa97@gmail.com','nayelisvargasmunoz@gmail.com','majojimenez2022@gmail.com','vargascamiloandres423@gmail.com','maryelesferreira@gmail.com','Andrewmunoz@idetp.edu.co','katianavergara56@gmail.com','luisalara648@gmail.com','juaquincaro0610@gmail.com','eduarcamargocamacho@gmail.com','klcastrillon8@misena.edu.co','guerra030201@gmail.com','camilaesther2002@gmail.com','0412vega.c@gmail.com','valdesvieris@gmil.com','charrisyerinel@gmail.com','Gpzh10@hotmail.com']
telefono=['3127490038','3014798600','5713468932','3006362050','3012340683','5713850505','5713329263','5713183687','3004071289','5718875777','3004156447','5713743259','3205406945','5713333333','5713911281','3159289668','3205894821','3004442019','3245367744','3014279721','3022819943','3653301000','3043096332','5713753590','5713662127','3138184920','3159289668','5718781103','3537373900','5713130987','3016714613','5713874501','3135523635','3126359526','3007910195','3003301550','3114357855','5713280558','3105198817','5713123456','1635485465','3006851823','3045799891','3014707130','5713737273','5552345000','3114618877','3006421333','3205680858','3107178731','5711111111','3008808270','3233361616','3003003448','30021903','3108605814','3205644371','5713003836','3004080417','5713030303','3217359041','5716503030','3014819993','3007882995','5713177049','3135697839','5713683653','3174832345','3013995751','314345687','3113295715','3205741191','5713623082','3219276670','3192145000','1668934000','3128106468','3002828233','5713244131','5713649515','5713026436','1234567000','3013156200','3106827022','3114184041','3245360991','3022101226','3145725805','5713750731','3006421333','3013797639','3006145546','5738211260']




def copy_clipboard():
        pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
        pya.hotkey('ctrl', 'c')
        time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
        return pyperclip.paste()

click=1
n=0

l=-1


def abrir():
    global l
    
    
    while n < len(cedula):
        l=l+1   
        robot.press("tab",presses=14)
        robot.typewrite(str(cedula[l]))
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
            time.sleep(5)
            
            
        else:
            
            robot.moveTo(posicion)
            robot.click(clicks=click)
            robot.press("tab",presses=18)
            robot.typewrite(str(nombres[l]))
            time.sleep(1)
            robot.press("tab",presses=1)
            robot.typewrite(str(apellido1[l]))
            time.sleep(1)
            robot.press("tab",presses=1)
            robot.typewrite(str(apellido2[l]))
            time.sleep(1)
            robot.press("tab",presses=1)
            robot.press("enter",presses=1)

            if (sexo[l]=="m"):
                pya.hotkey('down')
                robot.press("enter",presses=1)
            if (sexo[l]=="f"):
                pya.hotkey('down')
                pya.hotkey('down')
                robot.press("enter",presses=1)

            def copiarFecha():
                pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
                pyperclip.copy(fechanacimiento[l])
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
                robot.typewrite(telefono[l])# TELEFONO
                time.sleep(0.3)
                robot.press("tab",presses=8)
                time.sleep(0.3)

                def copiarCorreo():
                    pyperclip.copy("") 
                    pyperclip.copy(correo[l]) # personas a cargo
                    pya.hotkey('ctrl', 'c')
                    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                    return pyperclip.paste()
                    
                copiarCorreo()
                time.sleep(1)
                
                keyboard.press(Key.ctrl)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl) #pegar correo

                time.sleep(1)
                
                robot.press("tab",presses=1)
                robot.typewrite("Bachiller")# profesion
                robot.press("tab",presses=2)
                robot.press("enter",presses=1)
                time.sleep(5)
                robot.press("enter",presses=1)
                #https://agenciapublicadeempleo.sena.edu.co/spe-web/spe/oferta/new

                time.sleep(5)

                pya.hotkey('f6')
                pya.hotkey('del')


                def abrirnuevoregistro():
                    pyperclip.copy("") 
                    pyperclip.copy(consultar) # abrir nueva url
                    pya.hotkey('ctrl', 'c')
                    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                    return pyperclip.paste()
                    
                abrirnuevoregistro()
                time.sleep(1)
                
                keyboard.press(Key.ctrl)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl) #pegar url

                time.sleep(1)
                robot.press("enter",presses=1)
                time.sleep(5)

abrir()                                                                                                