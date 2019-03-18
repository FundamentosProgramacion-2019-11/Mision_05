#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#TRAZAR FIGURAS CON PYGAME

import random   # Calculos aleatorios
import math     # Libreria matematicas
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)        # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)              # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)              # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)                 # Negro es auscencia de color


def generarColor():  #Funcion que crea colores aleatorios
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    return (rojo, verde, azul)
def dibujarLineasEstrella(ventana):  #Funcion que crea o dibuja las lineas de la estrella
    for ladoSupIzquierdo in range (0,(ALTO//2),10): #para trazar lineas del lado izquierdo superior :)
        y= ladoSupIzquierdo+10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ladoSupIzquierdo,ALTO//2),(ANCHO//2,((ALTO//2)-y)))

    for ladoSupDerecho in range (0,(ALTO//2),10):
        y=ladoSupDerecho+10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ANCHO//2,ladoSupDerecho),(((ANCHO//2)+y),ALTO//2))

    for ladoInfIzquierdo in range (0,(ALTO//2),10):
        y=ladoInfIzquierdo+10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ladoInfIzquierdo,(ALTO//2)),((ANCHO//2),((ALTO//2)+y)))

    for ladoInfDerecho in range (0,(ALTO//2),10):
        y=ladoInfDerecho+10
        colorAleatorio= generarColor()
        pygame.draw.line(ventana, colorAleatorio,(((ANCHO)-ladoInfDerecho),(ALTO//2)),((ANCHO//2),((ALTO//2)+y)))
def dibujarEstrella():  #Funcion que dibuja la estrella
    pygame.init() # Inicializa el motor de pygame
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarLineasEstrella(ventana)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def cuadrosCirculos(ventana):
    for cuadrosY in range (0 , ALTO , 10):
        posicionX=cuadrosY+10
        posicionY=cuadrosY+10
        pygame.draw.line(ventana,NEGRO,((ANCHO//2)-posicionX,(ALTO//2)-posicionY),((ANCHO//2)+posicionX,(ALTO//2)-posicionY))
        pygame.draw.line(ventana,NEGRO,((ANCHO//2)-posicionX,(ALTO//2)+posicionY),((ANCHO//2)+posicionX,(ALTO//2)+posicionY))
    for cuadrosX in range (0 , ANCHO , 10):
        posicionX = cuadrosX + 10
        posicionY = cuadrosX + 10
        pygame.draw.line(ventana,NEGRO,((ANCHO//2)-posicionX,(ALTO//2)-posicionY),(((ALTO//2)-posicionX),(ALTO//2)+posicionY))
        pygame.draw.line(ventana,NEGRO,((ANCHO//2)+posicionX,(ALTO//2)-posicionY),(((ALTO//2)+posicionX),(ALTO//2)+posicionY))
    for circulos in range (0, (ALTO//2) ,10):
        radio=circulos+10
        pygame.draw.circle(ventana, NEGRO,(ANCHO//2, ALTO//2), radio, 1)
def dibujarCuadrosCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        cuadrosCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def laberinto (ventana):
    for linea in range (0 , (ANCHO//2)-10 , 10):
        lineahori= linea+10

        pygame.draw.line(ventana, NEGRO, (lineahori, lineahori),(ANCHO-lineahori,lineahori))              #horizontalsup
        pygame.draw.line(ventana, NEGRO, (ANCHO-linea, ALTO-lineahori),(lineahori,ALTO-lineahori)) #Horizontalinf
        pygame.draw.line(ventana, NEGRO, (lineahori,lineahori),(lineahori,ALTO-lineahori))                 #veticalizq
        pygame.draw.line(ventana, NEGRO, (ANCHO-lineahori,lineahori),(ANCHO-lineahori,ALTO-(lineahori+10)))     #verticalder
def dibujarLaberinto():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        laberinto(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def circulos(ventana):
    for circle in range(0,361,30):
        circles = (math.pi * circle) / 180
        x = int(math.sin(circles) * 150)
        y = int(math.cos(circles) * 150)
        pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)
def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        circulos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

def aproximacionPI(n):
    suma = 0
    for d in range(1, n + 1):  # 1,2,3,...,n
        fraccion = 1 / d ** 2
        suma += fraccion

    aproxPI = (6 * suma) ** 0.5
    return print ("Aproximado: ",aproxPI)

def divisiones3en19():
    total = 0
    for n in range (0,20):
        if n%3 == 0 :
            total += 1
    return print("Numeros divisibles entre 3, del 0 al 19: ", total)

def piramidesNumeros ():
    valor = 0
    for numero in range(1, 10):
        valor = valor * 10 + numero
        resultado = valor * 8 + numero
        print(valor, "* 8 ", "+", numero, "=", resultado)
    print("""
    """)
    valor2 = 1
    for numero in range(1, 10):
        resultado = valor2 * valor2
        valor2 = valor2 * 10 + 1
        print(valor2, "x", valor2,"=" ,resultado)


def funcionSalir():
    print("""
    ---------------------------------------------------    
    Menú, MISION 5:

        1.-Dibuja una Estrella
        2.-Dibuja Circulos y Cuadros
        3.-Dibuja Laberinto
        4.-Dibuja Circulos
        5.-Aproximar PI
        6.-Contar divisibles entre 19
        7.-Imprimir piramides de numeros
        0.-SALIR

    Introduzca el numero de la actividad que desea
    ---------------------------------------------------""")
    seleccion = int(input("¿Que desea hacer? "))
    return seleccion


def main ():
    seleccion= funcionSalir()

    while seleccion != 0:
        if seleccion == 1:
            dibujarEstrella()
        elif seleccion == 2:
            dibujarCuadrosCirculos()
        elif seleccion == 3:
            dibujarLaberinto()
        elif seleccion == 4:
            dibujarCirculos()
        elif seleccion == 5:
            aproximacionPI(90)
        elif seleccion == 6:
            divisiones3en19()
        elif seleccion == 7:
            piramidesNumeros()
        else:
            print("Intentelo de nuevo")
        seleccion= funcionSalir()
    print("¡Hasta luego!")

main()




