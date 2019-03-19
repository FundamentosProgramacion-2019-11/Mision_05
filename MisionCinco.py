#Sara Delgado González
#Misión 5

import pygame
from random import randint
from math import *

def dibujarCuadradosYCirculos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        negro = (0, 0, 0)

        for absisa in range(10, 801, 10):
            pygame.draw.rect(ventana, negro, (absisa, absisa, 800 - 2 * absisa, 800 - 2 * absisa), 1)

        for ordenada in range(10, 391, 10):
            pygame.draw.circle(ventana, negro, (ANCHO // 2, ALTO // 2), ordenada, 2)

        pygame.display.flip()
        reloj.tick(50)

    pygame.quit()

def dibujarEspiral():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    ROJO = (255,0,0)
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        posX = 400
        posY = 400

        for x in range(1, 159):
            y = x % 4
            contador = (((x % 2) + x) // 2) * 10
            if y == 1:
                pygame.draw.line(ventana, VERDE, (posX, posY), (posX + contador, posY + 0), 1)
                posX += contador
            elif y == 2:
                pygame.draw.line(ventana,  ROJO, (posX, posY), (posX + 0, posY - contador), 1)
                posY -= contador
            elif y == 3:
                pygame.draw.line(ventana, VERDE, (posX, posY), (posX - contador, posY + 0), 1)
                posX -= contador
            else:
                pygame.draw.line(ventana, ROJO, (posX, posY), (posX + 0, posY + contador), 1)
                posY += contador


        pygame.display.flip()
        reloj.tick(50)
    pygame.quit()
def dibujarCirculos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROSA = (255, 120, 210)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
       for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    termina = True
            ventana.fill(BLANCO)
            angulo = 0
            for i in range(1, 13):
                absisa = 150 * cos(angulo)
                ordenada = 150 * sin(angulo)
                pygame.draw.circle(ventana, ROSA, (400 + int(absisa), 400 + int(ordenada)), 150, 2)
                angulo += pi / 6

            pygame.display.flip()
            reloj.tick(50)
    pygame.quit()
def dibujarParabolas():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)
            for absisa in range(0, 401, 10):
                random = (randint(0, 255), randint(0, 255), randint(0, 255))
                pygame.draw.line(ventana, random, (400, absisa), (400 + absisa, 400),
                                 1)

                pygame.draw.line(ventana, random, (400, absisa), (400 - absisa, 400),
                                 1)

                pygame.draw.line(ventana, random, (400, 800 - absisa),
                                 (400 + absisa, 400), 1)

                pygame.draw.line(ventana, random, (400, 800 - absisa),
                                 (400 - absisa, 400), 1)

            pygame.display.flip()
            reloj.tick(50)
    pygame.quit()

def aproximarPI(proxdivisor):
    suma = 0
    for x in range(1, proxdivisor+1):
        suma += 1 / (x**2)
    pi = sqrt(6 * suma)
    return pi

def saberDivisibles():
    numero = 0
    for absisa in range(1000, 10000):
        if absisa % 37 == 0:
            numero += 1
    return numero

def imprimirPiramides():
    suma = 0
    for absisa in range(1, 10, 1):
        for y in range(absisa+1, 1, -1):
            suma += (10 ** y)//100
        print ("%d * 8 + %d = %d" % (suma, absisa, suma * 8 + absisa))
    print("\n")
    for t in range(0, 9, 1):
        num = 0
        for m in range(1, t+1, 1):
            num += 10**m
        num += 1
        print("%d * %d = %d" %(num, num, num * num))
def main():
    salir = False
    while not salir:
        print("""Tarea 5. Seleccione qué quiere hacer.
        1. Dibujar cuadrados y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar circulos
        5. Aproximar PI
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir""")
        respuesta = int(input("¿Qué desea hacer? "))

        if respuesta == 1:
            dibujarCuadradosYCirculos()
        elif respuesta == 2:
            dibujarParabolas()
        elif respuesta == 3:
            dibujarEspiral()
        elif respuesta == 4:
            dibujarCirculos()
        elif respuesta == 5:
            proxdivisor = int(input("Escriba el valor del divisor final: "))
            print("El valor aproximado de PI es:", aproximarPI(proxdivisor))
        elif respuesta == 6:
                print("Hay",saberDivisibles(), "números divisibles entre 19")
        elif respuesta == 7:
                imprimirPiramides()
        elif respuesta == 0:
            salir = True
        else:
            print("Error, escriba un número del 0 al 7")
main()
