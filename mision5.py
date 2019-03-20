#Roberto Castro Barrios A01748559
#Descripción: Programa que muestra un menú con diferentes acciones a realizar.

import random as r
import math as m
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)
def generarColorAleatorio ():
    rojo = r.randint(0, 255)
    verde = r.randint(0, 255)
    azul = r.randint(0, 255)
    return (rojo, verde, azul)

def dibujarDoceCirculos(ventana):
    for alfa in range(30, 361, 30):
        angRadianes = m.radians(alfa)
        x = 150 * m.cos(angRadianes)
        y = 150 * m.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(x+ANCHO//2), int(ALTO//2-y)), 150, 1)

def dibujarLineasEstrella(ventana):
    for y in range(0, ALTO//2, 10):
        xFinal = y + 10
        cRandom = generarColorAleatorio()
        pygame.draw.line(ventana, cRandom, (ANCHO//2, y), (ANCHO//2 + xFinal, ALTO//2))

    for y2 in range(0, ALTO//2, 10):
        xF2 = y2 + 10
        cRandom = generarColorAleatorio()
        pygame.draw.line(ventana, cRandom, (ANCHO//2, y2), (ANCHO//2 - xF2, ALTO//2))

    for y3 in range(0, ALTO//2, 10):
        xF3 = y3 + 10
        cRandom = generarColorAleatorio()
        pygame.draw.line(ventana, cRandom, (ANCHO//2, ALTO-y3), (ANCHO//2 - xF3, ALTO//2))

    for y4 in range(0, ALTO//2, 10):
        xF4 = y4 + 10
        cRandom = generarColorAleatorio()
        pygame.draw.line(ventana, cRandom, (ANCHO//2, ALTO-y4), (ANCHO//2 + xF4, ALTO//2))

def dibujarCC (ventana):
    for r in range (10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), r, 1)
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2-r, ALTO//2-r, r*2, r*2), 1)

# Estructura básica de un programa que usa pygame para dibujar
def dibujarEstrella ():
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
        dibujarLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def dibujarCirculos ():
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

        #dibujarDoceCirculos(ventana)
        dibujarDoceCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def dibujarCuadrosCirculos ():
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

        # dibujarDoceCirculos(ventana)
        dibujarCC(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def calcularPiramidesNumeros ():

    x = 0
    y = 0
    z = 0

    for factor in range(0, 9):
        base = 10**factor
        x = x + base
        y += x
        piramide = y * 8 + (factor+1)
        print(y, "* 8 +", factor+1, "=", piramide)

    for factor2 in range(0, 9):
        base2 = 10 ** factor2
        z = z + base2
        piramide2 = z + z
        print(z, "*", z, "=", piramide2)

def aproximarPI (n):
    suma = 0
    for d in range(1, n+1): #1,2,3...n
        fraccion = (1/d**2)
        suma += fraccion

    aproxPi = (6*suma) ** 0.5
    return aproxPi

def esDivisibleEntre37 (n):
    cociente = n%37 == 0
    return cociente

def main ():
    print ("Misón 5. Seleccione qúe quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar círculos")
    print("4. Aproximar PI")
    print("5. Contar divisibles entre 37")
    print("6. Imprimir pirámides y números")
    print("0. Salir")
    salir = False
    while not salir != 0:
        accion = int(input("¿Qué desea hacer? "))
        if accion == 1:
            dibujarCuadrosCirculos()

        elif accion == 2:
            dibujarEstrella()

        elif accion == 3:
            dibujarCirculos()

        elif accion == 4:
            n = int(input("Ingresa un valor para aproximar a pi: "))
            if n == 0:
                print("El valor es incorrecto")
            else:
                aproxPi = aproximarPI(n)
                print("La aproximación más cercana con el número %d es: %f"%(n, aproxPi))

        elif accion == 5:
            div = 0
            for n in range(1, 10000):
                if esDivisibleEntre37(n):
                    div = div + 1
                else:
                    div = div + 0
            print("%d números de 4 dígitos son divisibles entre 37"%(div))

        elif accion == 6:
            calcularPiramidesNumeros()
        else:
            salir = True

main()
