# Autor: Guillermo De Anda Casas , A01375892
# Programa que contiene los códigos para cada ejercicio de la Misión 5 y un menú para controlarlos.


import math
import random
import pygame


ANCHO = 800
ALTO = 800


BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


def generarColor(): # Función que genera un color aleatorio para pygame.
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    return (rojo, verde, azul)


def dibujar(opcion): # Función que recibe la opción del menú seleccionada y controla solamente a las funciones de pygame.
    if opcion == 1:
        dibujarCuadrosCirculos()
    elif opcion == 2:
        dibujarEstrella()
    elif opcion == 3:
        dibujarEspiral()
    elif opcion == 4:
        dibujarCirculos()


def dibujarEspiral(): # Función que dibuja la espiral de líneas rectas (cuadrados) en pygame.
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        y = 10
        while y <= 390:
            pygame.draw.line(ventana, NEGRO, (800 - y, 800 - y), (y, 800 - y), 1)
            pygame.draw.line(ventana, NEGRO, (y, 800 - y), (y, y), 1)
            pygame.draw.line(ventana, NEGRO, (y, y), (800 - y, y), 1)
            pygame.draw.lines(ventana, NEGRO, False, [(800 - y, y), (800 - y, 800 - y - 10), (800-y-10, 800 - y - 10)], 1)
            y += 10

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarCuadrosCirculos(): #Función que crea la imágen de cuadros y círculos concéntricos.
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for y in range(0, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (y, y, 800 - (y * 2), 800 - (y * 2)), 1)

        for radio in range(10, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarCirculos(): # Función que dibuja la flor de círculos en pygame.
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for alfa in range(30, 390, 30):
            angRadianes = math.radians(alfa)
            x = 150 * math.cos(angRadianes)
            y = 150 * math.sin(angRadianes)
            pygame.draw.circle(ventana, NEGRO, (int(x + ANCHO // 2), int(y + ALTO // 2)), 150, 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarEstrella(): # Función que dibuja la estrella en pygame.
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for y in range(0, 400, 10):
            x2 = y + 410
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (400, y), (x2, 400))
        for y in range(0, 400, 10):
            x2 = y + 410
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (y, 400), (400, x2))
        for y in range(0, 400, 10):
            x2 = 400 - y
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (400, y), (x2, 400))
        for y in range(0, 400, 10):
            x2 = 800 - y
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (400, y + 400), (x2, 400))

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def aproximarPi(divisor): # Función que calcula el valor aporximado de pi, recibiendo el último divisor de la fórmula.
    suma = 0
    for d in range(1, divisor):
        fraccion = 1 / d ** 2
        suma += fraccion
    aproxPI = (6 * suma) ** 0.5
    return aproxPI


def esDivisible37(): # Función que calcula la cantidad de números de 4 dígitos, divisibles entre 37.
    numeros = 0
    for n in range(1000, 10000):
        if n % 37 == 0:
            numeros += 1
    cantidad = numeros
    return cantidad


def piramideNumeros(): # Función que genera las pirámides de números.
    factorUno = 0
    factorDos = 0
    for n in range(0,9):
        suma = 1 + (10 ** n)
        factorUno += suma - (1 ** n)
        factorDos += factorUno
        resultado = (factorDos * 8) + (n+1)
        print(factorDos, "* 8 +", (n+1), "=", resultado)

    factorTres = 0
    for n in range(0, 9):
        sumaDos = 10 ** n
        factorTres += sumaDos
        resultadoDos = factorTres * factorTres
        print(factorTres, "*", factorTres, "=", resultadoDos)


def main(): # Función main que genera el menú y controla a todas las demás.
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar estrella")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 37")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    while opcion != 0:
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
            dibujar(opcion)
        elif opcion == 5:
            divisor = int(input("¿Cuál es el último divisor? "))
            print(aproximarPi(divisor))
        elif opcion == 6:
            print(esDivisible37(), "números de 4 dígitos son divisibles entre 37")
        elif opcion == 7:
            print(piramideNumeros())
        print("Misión 5. Seleccione qué quiere hacer.")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar estrella")
        print("3. Dibujar espiral")
        print("4. Dibujar círculos")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 37")
        print("7. Imprimir pirámides de números")
        print("0. Salir")
        opcion = int(input("¿Qué desea hacer? "))


main() # Llamada a la función main.