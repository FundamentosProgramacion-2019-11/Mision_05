# Autor: Rosalía Serrano Herrera
# Pregunta al usuario qué desea que el programa ejecute


import pygame
import random
import math


ANCHO = 800
ALTO = 800
#Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


def dibujarCuadrosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for radio in range(1, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), (ANCHO//2)-radio, 1)
        for centro in range(1, ALTO //2, 10):
            pygame.draw.rect(ventana, NEGRO, (centro, centro,ANCHO-(2*centro),ALTO-(2*centro)), 1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


def generarColorAzar():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo, verde, azul)
    return colorX


def dibujarEstrella():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
       for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

    ventana.fill(BLANCO)

    for x in range(0, ANCHO//2 + 1, 10):  # 10, 20, 30.... ANCHO
        colorX = generarColorAzar()
        pygame.draw.line(ventana, colorX, (x, 400), (400, 400 - x), 1)
        pygame.draw.line(ventana, colorX, (400 + x, 400), (400, x), 1)
        pygame.draw.line(ventana, colorX, (x, 400), (400, 400 + x), 1)
        pygame.draw.line(ventana, colorX, (400 + x, 400), (400, ANCHO - x), 1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ANCHO // 2 + x), (405 + x, ANCHO // 2 + x), 1)
            pygame.draw.line(ventana, NEGRO, (390 - x, 390 - x), (ANCHO // 2 - x - 10, ANCHO // 2 + x + 10), 1)

        for y in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (400 - y - 10, 390 - y), (400 + y + 5, 400 - y - 10), 1)
            pygame.draw.line(ventana, NEGRO, (400 + y + 5, 400 + y), (400 + y + 5, 400 - y - 10), 1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for alfa in range(12):
            x = int(150 * math.cos(math.radians(-30 * (alfa + 1))))
            y = int(150 * math.sin(math.radians(-30 * (alfa + 1))))
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + x , ALTO // 2 + y), 150, 1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


def aproximarPI(valor):
    suma = 0    #La sumatoria de fracciones
    for n in range(1, valor+1):
        fraccion = 1 / n**2
        suma += fraccion

    suma = suma*6
    PI = suma ** 0.5
    return PI


def calcularDivisibles():
    numeros = 0
    for divisibles in range (1000, 10000):
        if divisibles % 37 == 0:
            numeros += 1
    return numeros


def imprimirPiramides():
    contador = 1
    acumulador1 = 1
    acumulador2 = 1

    for primera in range(1, 10):
        cuenta = acumulador1 * 8 + contador
        print(acumulador1, "* 8 +", contador, "=", cuenta)
        contador = contador + 1
        acumulador1 = acumulador1 * 10 + contador

    for segunda in range(1, 10):
        total = acumulador2 ** 2
        print(acumulador2, "*", acumulador2, "=", total)
        acumulador2 = acumulador2 * 10 + 1


def main():
    print("Misión 5. Seleccione qué quiere hacer:", "\n", "1. Dibujar cuadros y círculos", "\n", "2. Dibujar estrella", "\n", "3. Dibujar espiral", "\n", "4. Dibujar círculos", "\n", "5. Aproximar PI", "\n", "6. Contar divisibles entre 37", "\n", "7. Imprimir pirámides de números", "\n", "0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    while opcion !=0:
        if opcion == 1:
            dibujarCuadrosCirculos()
        elif opcion == 2:
            dibujarEstrella()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            valor = int(input("¿Cuál es el número que quieres aproximar a PI? "))
            PI = aproximarPI(valor)
            print("La aproximación a PI es:", PI)
        elif opcion == 6:
            divisibles = calcularDivisibles()
            print("Los números de 4 dígitos divisibles entre 37 son:", divisibles)
        elif opcion == 7:
            (imprimirPiramides())
        else:
            print("Por favor, introduce una opción válida")

        opcion = int(input("¿Qué desea hacer? "))


main()