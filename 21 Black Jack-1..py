# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180125-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).
from tkinter import *
from random import randint
from time import sleep

# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducci�n no es correcta.

# valor actual de las cartas,c_m <- cartas que debe mostrar
def print_c(t, c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_m):
    i = int()
    j = int()
    x = int()
    n_cart = int()
    cartas_en_mesa = int()
    carta_1 = int()
    carta_2 = int()
    carta_3 = int()
    carta_4 = int()
    carta_5 = int()
    carta_6 = int()
    carta_7 = int()
    carta_8 = int()
    carta_9 = int()
    carta_10 = int()
    cartas = str()
    a = str()
    b = str()
    c = str()
    d = str()
    e = str()
    f = str()
    g = str()
    n = str()
    reng = str()
    reng = [[str() for ind0 in range(5)] for ind1 in range(4)]
    cartas = [[str() for ind0 in range(50)] for ind1 in range(4)]
    cartas_en_mesa = c_m
    n_cart = (5*cartas_en_mesa)-1
    x = 0
    # son los caracteres que forman las figuras de las cartas
    n = "?"
    a = "|"
    b = "_"
    c = "|"
    d = "|"
    e = ""
    f = " "
    g = "_"
    reng[0][0] = f
    reng[0][1] = b
    reng[0][2] = b
    reng[0][3] = b
    reng[0][4] = f
    reng[1][0] = a
    reng[1][1] = f
    reng[1][2] = f
    reng[1][3] = f
    reng[1][4] = a
    reng[2][0] = a
    reng[2][1] = f
    reng[2][2] = n
    reng[2][3] = f
    reng[2][4] = a
    reng[3][0] = c
    reng[3][1] = g
    reng[3][2] = b
    reng[3][3] = g
    reng[3][4] = d
    # genera un arreglo que muestra 10 cartas en 4 renglones cada una, una al lado de la otra
    for i in range(4):
        for j in range(50):
            if x<5:
                cartas[i][j] = reng[i][x]
                x = x+1
            if x>4:
                x = 0
    carta_1 = c_1
    carta_2 = c_2
    carta_3 = c_3
    carta_4 = c_4
    carta_5 = c_5
    carta_6 = c_6
    carta_7 = c_7
    carta_8 = c_8
    carta_9 = c_9
    carta_10 = c_10
    # si el numero tiene 2 cifras ajusta el espacio para que no se deforme la carta
    if carta_1>9:
        cartas[2][1] = e
    if carta_2>9:
        cartas[2][6] = e
    if carta_3>9:
        cartas[2][11] = e
    if carta_4>9:
        cartas[2][16] = e
    if carta_5>9:
        cartas[2][21] = e
    if carta_6>9:
        cartas[2][26] = e
    if carta_7>9:
        cartas[2][31] = e
    if carta_8>9:
        cartas[2][36] = e
    if carta_9>9:
        cartas[2][41] = e
    if carta_10>9:
        cartas[2][46] = e
    # guartda el valor en el lugar que correspnde para que se imprima en el centro de la carta
    cartas[2][2] = str(carta_1)
    cartas[2][7] = str(carta_2)
    cartas[2][12] = str(carta_3)
    cartas[2][17] = str(carta_4)
    cartas[2][22] = str(carta_5)
    cartas[2][27] = str(carta_6)
    cartas[2][32] = str(carta_7)
    cartas[2][37] = str(carta_8)
    cartas[2][42] = str(carta_9)
    cartas[2][47] = str(carta_10)
    # hace que en la primer mano, el valor de la segunda carta de la mesa no sea visible
    if cartas_en_mesa<3 and t==0:
        cartas[2][7] = n
        if carta_2>9:
            cartas[2][6] = f
    # imprime los cuatro renglones de las cartas
    for i in range(4):
        # n_cart indica el numero de cartas que debe mostrar
        for j in range(n_cart+1):
            if j==0:
                # deja un espacio antes de la primer carta
                print ("              ",cartas[i][j],end="")
            else:
                if (1+j)%5==0:
                    # deja un espacio entre las cartas
                    print (cartas[i][j]," ",end="")
                else:
                    print (cartas[i][j],end="")
        print ("")
    print ("")
    print ("")

# deja "num" lineas en blanco
def espacio(num):
    i = int()
    for i in range(1,num+1):
        print (" ",end="")
    print ("")

# imprime una linea separadora de largo "num"
def linea(num):
    i = int()
    for i in range(1,num+1):
        print ("__",end="")
    print ("")

# elije la carta num de las 20 repartidas al azar
def cart(jugadas, num):
    carta = int()
    carta = jugadas[num]
    return carta

# si el ususario pone si, imprime las reglas del juego
def reglas():
    resp = str()
    print (" Si desea leer las reglas del juego escriba si, para")
    print ("  comenzar el juego presione enter.")
    resp = input()
    if resp=="si":
        print ("" )# no hay forma directa de borrar la pantalla con Python estandar
        espacio(1)
        print ("Reglas del juego: ")
        espacio(1)
        print ("El objetivo del juego es sumar 21 puntos o llegar los mas cerca posible sin pasarse")
        print ("En caso de que los jugadores no lleguen a 21, quien quede mas cerca gana")
        espacio(1)
        print ("La mesa reparte inicialmente 2 cartas a los jugadores y 2 para la mesa, ")
        print ("la segunda carta de la mesa permanece oculta hasta que el jugador termine su mano")
        print ("una vez repartidas las cartas iniciales, el jugador podra pedir ")
        print ("carta, hasta que se plante, o se pase de 21")
        espacio(1)
        print ("Puntajes: Las cartas mayores a 9 suman 10 puntos, los ases suman 1 punto u 11, segun convenga, el resto de las cartas ")
        print ("suman su valor numerico")
        print ("Si el jugador obtiene en las dos primeras cartas la suma de 21 se considera Black Jack automaticamente gana la partida")
        espacio(1)
        print ("Apuestas: Las apuesas se realizan antes de repartir las cartas")
        espacio(1)
        print ("Pago: A los jugadores que hacen Black Jack se les paga 3 a 1 su apuesta, a los que ganen ")
        print ("en el transcurso de la partida se les paga el mismo valor de la apuesta")
        print ("En caso de empate, se devuelve el valor de la apuesta")
        espacio(1)
        print ("  Para comenza el juego presione enter.")
        input() # a diferencia del pseudoc�digo, espera un Enter, no cualquier tecla

if __name__ == '__main__':
    reglas()
    print ("") # no hay forma directa de borrar la pantalla con Python estandar
    finjuego = bool()
    se_planta = bool()
    b_j = bool()
    w_mesa = bool()
    w_jug = bool()
    empate = bool()
    esentero = bool()
    sin_dinero = bool()
    car_1 = int()
    car_2 = int()
    car_3 = int()
    car_4 = int()
    car_5 = int()
    car_6 = int()
    car_7 = int()
    car_8 = int()
    car_9 = int()
    car_10 = int()
    cartas_jug = int()
    mano = int()
    cartas_mesa = int()
    chang = int()
    chang_m = int()
    var = int()
    baraja = int()
    jugadas = int()
    i = int()
    j = int()
    x = int()
    n = int()
    a = int()
    b = int()
    c = int()
    d = int()
    e = int()
    f = int()
    caja = int()
    apuesta = int()
    puntos_j = int()
    puntos_m = int()
    cont = int()
    cont_m = int()
    n_juegos = int()
    seguir_jugando = str()
    resp = str()
    exclamacion = str()
    mens_1 = str()
    mens_2 = str()
    mens_3 = str()
    mens_4 = str()
    mens_5 = str()
    mens_6 = str()
    mens_7 = str()
    mens_8 = str()
    mens_9 = str()
    mens_10 = str()
    mens_11 = str()
    mens_12 = str()
    mens_13 = str()
    mens_14 = str()
    mens_15 = str()
    mens_16 = str()
    opc = str()
    apuest = str()
    vx = str()
    # solo para inicializar la variable
    seguir_jugando = "si"
    sin_dinero = False
    mens_1 = "  Hola, bienbenido a 21, Suerte!!"
    mens_2 = "  Cuanto quieres apostar en esta mano? "
    mens_3 = " Lamentablemente no dispones de tanto dinero, debes apostar menos de: "
    mens_4 = "  Tus cartas son: "
    mens_5 = "  La primer carta de la mesa es: "
    mens_6 = "  Para pedir otra carta responder 's', o presiona Enter para plantarse"
    mens_7 = " Tu apuesta actual es de: "
    mens_8 = " Lamentablemente en esta mano has perdido :("
    mens_9 = "   Felicidades, le ganaste a la mesa!!!!"
    mens_10 = "  El valor de la apuesta debe ser un Numero mayor que cero y menor que "
    mens_11 = " Para que el juego tenga un poco de gracia deberias apostar algo mas "
    mens_12 = " Felicidades, has sacado 21 en la primer mano y le ganaste a la mesa"
    mens_13 = " En este caso el valor de tu apuesta se triplica, has ganado: $"
    mens_14 = "  ups perdiste, te has pasado de 21 "
    mens_15 = " Has ganado: $"
    mens_16 = " Esta mano ha terminado en empate, te devolvemos tu apuesta"
    caja = 1500
    apuesta = 1
    exclamacion = "!!!"
    # aca se guardan las 20 cartas al azar
    jugadas = [int() for ind0 in range(20)]
    # maso de cartas
    baraja = [int() for ind0 in range(48)]
    n = 1
    x = 0
    n_juegos = 0
    # mientras el jugador quiera seguir y tenga aun dinero
    while seguir_jugando!="no" and sin_dinero==False:
        print ("") # no hay forma directa de borrar la pantalla con Python estandar
        finjuego = False
        se_planta = False
        # se vuelven a iniciar algunas variables, menos caja
        puntos_j = 0
        puntos_m = 0
        w_mesa = False
        w_jug = False
        empate = False
        b_j = False
        cont = 1
        cont_m = 12
        chang = 0
        chang_m = 0
        x = 0
        # cada 2 jugads se vuelve el maso a su estado inicial
        if n_juegos==0 or n_juegos%2==0:
            # una vez por cada palo
            for i in range(4):
                # primera carta de cada palo
                n = 1
                for j in range(12):
                    baraja[x] = n
                    # x recorre las 48 cartas del maso 
                    x = x+1
                    n = n+1
                    # guarda en el maso 12 cartas x 4 palos
        i = 0
        # reparte 20 cartas al azar de 48 disponibles en el maso
        while i<20:
            x = randint(0,47)
            if baraja[x]!=0:
                # guarda las 20 cartas en jugadas
                jugadas[i] = baraja[x]
                # evita que se repitan las cartas del maso
                baraja[x] = 0
                i = i+1
        # contador de juegos, se vuelve  a cear el maso de cartas cada 2 juegos
        n_juegos = n_juegos+1
        print (mens_1,exclamacion)
        espacio(1)
        print ("                                  Dinero disponible: ",caja)
        espacio(1)
        while True:# no hay 'repetir' en python
            print (mens_2)
            apuest = input()
            # Validar si es un numero
            esentero = True
            # 123
            n = len(apuest)
            i = 0
            while ((i<n) and (esentero)):
                vx = apuest[i:i+1]
                esentero = (vx=="0") or (vx=="1") or (vx=="2") or (vx=="3") or (vx=="4") or (vx=="5") or (vx=="6") or (vx=="7") or (vx=="8") or (vx=="9") or (vx=="-")
                i = i+1
            if not (esentero):
                print ("") # no hay forma directa de borrar la pantalla con Python estandar
                print (" Debe ingresar un numero: ")
            if esentero:
                apuesta = float(apuest)
            if apuesta>caja:
                print ("") # no hay forma directa de borrar la pantalla con Python estandar
                espacio(1)
                print (mens_3,caja,exclamacion)
                espacio(1)
                sleep(2)
                esentero = False
            if apuesta==0:
                print (mens_11)
                esentero = False
            if (esentero): break
        print ("") # no hay forma directa de borrar la pantalla con Python estandar
        caja = caja-apuesta
        #print ("                                  Dinero disponible: ",caja)
        #print (mens_7,apuesta)
        espacio(1)
        # numero de cartas que se muetran en la primer mano al jugador
        cartas_jug = 2
        # numero de cartas que se muestran en la primer mano a la mesa
        cartas_mesa = 2
        mano = 0
        # desarrollo del juego
        while finjuego==False:
            print ("") # no hay forma directa de borrar la pantalla con Python estandar
            print ("                                  Dinero disponible: ",caja)
            print (mens_7,apuesta)
            espacio(1)
            # acumula los puntos de la primer carta de la mesa
            if mano==0 and cartas_jug<3:
                # si la carta es ditinta de uno y menor a diez
                if cart(jugadas,11)!=1 and cart(jugadas,11)<10:
                    # suma el valor de la carta
                    puntos_m = puntos_m+cart(jugadas,11)
                else:
                    # si la primer carta es 1 vale 11
                    if cart(jugadas,11)==1:
                        puntos_m = puntos_m+11
                        # cambia la variable que permite volver el 11 a 1 si es conveniente
                        chang_m = chang_m+1
                    else:
                        # si vale 10 o mas se suman 10
                        if cart(jugadas,11)>9:
                            puntos_m = puntos_m+10
            # almacena en la variable car_n el valor de la carta que le toco a la mesa para imprimirla
            car_1 = cart(jugadas,11)
            # para la mesa se sacaron las cartas del 10 al 19
            car_2 = cart(jugadas,12)
            car_3 = cart(jugadas,13)
            car_4 = cart(jugadas,14)
            car_5 = cart(jugadas,15)
            car_6 = cart(jugadas,16)
            car_7 = cart(jugadas,17)
            car_8 = cart(jugadas,18)
            car_9 = cart(jugadas,19)
            car_10 = cart(jugadas,10)
            # se ejecuta luego de la mano del jugador
            if se_planta==True:
                mano = mano+1
                # se evalua el valor de la segunda carta de la mesa
                if cart(jugadas,12)==1:
                    if puntos_m<11:
                        puntos_m = puntos_m+11
                        chang_m = chang_m+1
                    else:
                        puntos_m = puntos_m+1
                else:
                    if cart(jugadas,12)<10:
                        puntos_m = puntos_m+cart(jugadas,12)
                    else:
                        puntos_m = puntos_m+10
                # si se pasa de 21 y hay un 1 con valor 11, lo vuelve a uno
                if puntos_m>21 and chang_m!=0:
                    puntos_m = puntos_m-10
                    chang_m = chang_m-1
            # luego de la mano del jugador y de descubrir la segunda carta de la mesa
            if mano>1 and se_planta==True:
                # a partir de la tercer carta de la mesa
                i = 13
                # la mesa deja de sacar cartas cuando llega a 17
                while puntos_m<=17 and puntos_m<puntos_j:
                    if cart(jugadas,i)==1:
                        if puntos_m<11:
                            puntos_m = puntos_m+10
                            chang_m = chang_m+1
                        else:
                            puntos_m = puntos_m+1
                    else:
                        if cart(jugadas,i)<10:
                            puntos_m = puntos_m+cart(jugadas,i)
                        else:
                            puntos_m = puntos_m+10
                    if puntos_m>21 and chang_m!=0:
                        puntos_m = puntos_m-10
                        chang_m = chang_m-1
                    # aumenta la cantidad de cartas a mostrar para mesa
                    cartas_mesa = cartas_mesa+1
                    # pasa a la siguiente carta
                    i = i+1
                # cuando alcanza 17 puntos o mas termina el juego
                finjuego = True
            print ("  Las cartas de la mesa son: ")
            print_c(mano,car_1,car_2,car_3,car_4,car_5,car_6,car_7,car_8,car_9,car_10,cartas_mesa)
            print ("  Las catras de la mesa suman:  ",puntos_m," puntos")
            linea(28)
            espacio(1)
            # valor de las 10 cartas del jugador
            car_1 = cart(jugadas,1)
            # son las cartas del 0 al 9 de las seleccionadas al azar
            car_2 = cart(jugadas,2)
            car_3 = cart(jugadas,3)
            car_4 = cart(jugadas,4)
            car_5 = cart(jugadas,5)
            car_6 = cart(jugadas,6)
            car_7 = cart(jugadas,7)
            car_8 = cart(jugadas,8)
            car_9 = cart(jugadas,9)
            car_10 = cart(jugadas,0)
            espacio(1)
            print ("  Tus cartas son: ")
            espacio(1)
            # mientras pida mas cartas
            if se_planta==False:
                # cont inicial vale uno, accion para la carta uno
                for i in range(cont,cartas_jug+1):
                    if puntos_j<11 and cart(jugadas,i)==1:
                        # si sale un uno y es conveniente cambia a 11
                        var = cart(jugadas,i)
                        var = 11
                        # esta variable indica que hay un uno que vale 11 en caso de que se pase se puede restar 10
                        chang = chang+1
                        puntos_j = puntos_j+var
                    else:
                        # si tiene 11 pntos o mas el uno vale uno
                        if puntos_j>10 and cart(jugadas,i)==1:
                            puntos_j = puntos_j+cart(jugadas,i)
                    # si la carta es 10 o mas,se suman 10 puntos
                    if cart(jugadas,i)>9:
                        puntos_j = puntos_j+10
                    else:
                        # si no es mayor a 9 y es distinta de uno, se suma el valor de la carta
                        if cart(jugadas,i)!=1:
                            puntos_j = puntos_j+cart(jugadas,i)
                    # si se paso de 21 y hay algun 1 con valor 11, se restan 10(el uno vuelve a valer uno)
                    if puntos_j>21 and chang>0:
                        puntos_j = puntos_j-10
                        chang = chang-1
                    cont = cont+1
            # imprime las cartas del jugador
            print_c(1,car_1,car_2,car_3,car_4,car_5,car_6,car_7,car_8,car_9,car_10,cartas_jug)
            print ("  Tus cartas suman: ",puntos_j," puntos.")
            # solo para inicializar la variable
            opc = "fin"
            # si es la primer mano y obtinene 21 gana
            if cartas_jug==2 and puntos_j==21 and puntos_m<21 and se_planta==False:
                caja = caja+apuesta*3
                print (mens_12)
                print (mens_13,apuesta*3)
                print ("                                  Dinero disponible: ",caja)
                # termina el juego
                finjuego = True
                se_planta = False
                # variable para no volver a sumar la caja terminado el juego
                b_j = True
            # mientras no se pase de 21 y pida otra carta
            if puntos_j<21 and se_planta==False:
                print (mens_6)
                opc = input()
            # si piede mas cartas
            if opc=="s" and puntos_j<21:
                finjuego = False
                # incementa l numero de cartas a mostrar para el jugador
                cartas_jug = cartas_jug+1
            # si no pide mas cartas y no se pasa de 21, se planta
            if puntos_j<=21 and opc!="si":
                se_planta = True
            if se_planta==True:
                # sale de la mano 0 para el jugador, la mesa ahora mostrara sus 2 cartas a la vista
                mano = mano+1
            # Borrar Pantalla;
            # si se pasa de 21 trmina el juego
            if puntos_j>21:
                finjuego = True
            if caja==0:
                sin_dinero = True
        espacio(2)
        linea(28)
        # si el jugador se pasa de 21 gana la mesa
        if puntos_j>=22:
            w_mesa = True
        # cuando no se paso y no tiene 21 en la primer mano(la apuesta se paga distinto)
        if puntos_j<=21 and b_j==False:
            # si la mesa tine menos puntos, o si la mesa se pasa gana jugador
            if puntos_j>puntos_m or puntos_m>=22:
                w_jug = True
            else:
                # si no se pasa y empata con la mesa -empate
                if puntos_j==puntos_m:
                    empate = True
                else:
                    # en otro caso gana la mesa
                    w_mesa = True
        if empate:
            print (mens_16)
            caja = caja+apuesta
        else:
            if w_mesa:
                print (mens_8)
            else:
                # esta prte no se ejecuta si el jugador obtiene 21 en la primer mano, la apuesta se paga distinta
                if b_j==False:
                    print (mens_9)
                    print (mens_15,apuesta)
                    espacio(1)
                    caja = caja+(apuesta*2)
        if caja>0:
            sin_dinero = False
        if sin_dinero==False:
            linea(28)
            print ("  Quieres seguir jugando?")
            espacio(1)
            print ("  Escriba no para salir, presione enter para seguir jugando")
            seguir_jugando = input()
        else:
            print (" y te quedaste sin dinero")

