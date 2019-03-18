#Autor: María Fernanda García Gastélum A01376181
#Completar mision 5

import math
import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0, 0, 0)


def generarColor():
    rojo = random.randint(0, 255)
    verde= random.randint(0, 255)
    azul= random.randint(0, 255)

    return (rojo, verde, azul)


def dibuajarLineasEstrella(ventana):
    for y in range(0, ALTO//2, 10): #Inferior Izquierdo
        xFinal= y +10
        colorAleatorio= generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y+400), (xFinal, ALTO//2))
    for y in range(0, ALTO // 2, 10): #Superior Derecho
        xFinal = y + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y), (xFinal+400, 400))
    for y in range(0, ALTO // 2, 10): #Superior Izquierdo
        xFinal = 400-y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y), (xFinal, 400))
    for y in range(0, ALTO // 2, 10): #Inferior Derecjo
        xFinal = 800-y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y+400), (xFinal, 400))


def dibujarEstrella():
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
        dibuajarLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCirculosDeCuadros(ventana):
    for radio in range (10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)


def dibujarCuadros(ventana):
    for x in range(1, ANCHO//2, 2):
        pygame.draw.rect(ventana, NEGRO, [ANCHO//2-(5*x), ALTO//2-(5*x), 10*x, 10*x], 1)


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
        dibujarCuadros(ventana)
        dibujarCirculosDeCuadros(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarDoceCirculos(ventana):

    for alfa in range (30, 390, 30):
        angRadianes= math.radians(alfa)
        x= 150*math.cos(angRadianes)
        y = 150 * math.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(x+ANCHO//2), int(ALTO//2-y)), 150, 1)


def dibujarCirculo():
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
        dibujarDoceCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def aproximarPI(divisibles):
    suma=0
    for d in range(1, divisibles+1): #1, 2, 3... n
        fraccion= 1/(d**2)
        suma += fraccion
    aproxPI = (6 * suma) ** 0.5
    return aproxPI


def contarDivisibles():
    divisores=0
    for d in range(1000, 10000):
        if d % 37 == 0:
            divisores += 1
    return divisores


def imprimirPiramides():
    piramide2 = 0
    numero = 0
    for n in range(0, 9):
        suma2 = 1 + (10**n)
        piramide2 += suma2 - 1**n
        numero += piramide2
        producto= numero*8+(n+1)
        print(numero, "* 8 +", (n+1), "=", producto)
    piramide1 = 0

    for n in range(0, 9):
        suma = 10 ** n
        piramide1 += suma
        producto = piramide1 * piramide1
        print(piramide1, "*", piramide1, "=", producto)


def main():
    print("Misión 5. Seleccione que quiere hacer.")
    print("1. Dibujar cuadros y círculos.")
    print("2. Dibujar parábolas.")
    print("3. Dibujar circulos.")
    print("4. Aproximar PI.")
    print("5. Contar divisibles entre 37.")
    print("6. Imprimir pirámides de números.")
    print("0. Salir.")
    n = int(input("Qué desea hacer: "))
    while n >= 0 and n <= 7:
        if n==1:
            dibujarCuadrosCirculos()
        elif n==2:
            dibujarEstrella()
        elif n==3:
            dibujarCirculo()
        elif n==4:
            divisibles = int(input("Número de divisibles que se desea aproximar:"))
            x = aproximarPI(divisibles)
            print(x)
        elif n==5:
            y = contarDivisibles()
            print(y)
        elif n==6:
            imprimirPiramides()
        elif n==0:
            exit()
        else:
            "Error"
        print("Misión 5. Seleccione que quiere hacer.")
        print("1. Dibujar cuadros y círculos.")
        print("2. Dibujar parábolas.")
        print("3. Dibujar circulos.")
        print("4. Aproximar PI.")
        print("5. Contar divisibles entre 37.")
        print("6. Imprimir pirámides de números.")
        print("0. Salir.")
        n = int(input("Qué desea hacer: "))


main()


