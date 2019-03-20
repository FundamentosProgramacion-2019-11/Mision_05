# encoding: UTF-8
# Autor: Ronaldo Estefano Lira Buendia
# Programa donde atraves de un menu, ejecutas cualquiera de las opciones disponibles.

import pygame
import random
import math

ANCHO = 800
ALTO = 800

NEGRO = (0, 0, 0) #000000
BLANCO = (255, 255, 255) #FFFFFF

def dibujar(x):
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        if x==1:
            dibujarCuadrosCirculos(ventana)
        elif x==2:
            dibujarEstrella(ventana)
        elif x==3:
            dibujarCirculos(ventana)
        else:
            pass

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def generarColorAlazar():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo, verde, azul)
    return colorX


def dibujarCuadrosCirculos(ventana):
    for y in range(0, 400, 10):
        pygame.draw.rect(ventana, NEGRO, (395-y, 395-y, 10+(2*y), 10+(2*y)), 1)
    for y in range(10, 400, 10):
        pygame.draw.circle(ventana, NEGRO, (400, 400), y, 1)

def dibujarArco1(ventana):
    for x in range(400,ANCHO+1,10):
        y = ALTO-x+400
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArco2(ventana):
    for x in range(0,400+1,10):
        y = 400+x
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArco3(ventana):
    for x in range(0,400+1,10):
        y = 400-x
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArco4(ventana):
    for x in range(400,ANCHO+1,10):
        y = x-410
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))


def dibujarEstrella(ventana):
    dibujarArco1(ventana)
    dibujarArco2(ventana)
    dibujarArco3(ventana)
    dibujarArco4(ventana)


def dibujarCirculos(ventana):
    for y in range(0, 360, 30):
        x = y
        angulosR = math.radians(x)
        x = 150 * math.cos(angulosR)
        y = 150 * math.sin(angulosR)
        pygame.draw.circle(ventana, NEGRO,(int(x+(ALTO//2)), int(y + (ALTO // 2))), 150, 1)


def aproximarPI(y):
    contador = 0
    for x in range(1, y+1 ,1):
        contador += (1/(x ** 2))
    pi = (contador * 6)**.5
    return pi


def calcularDivisibles37():
    contador = 0
    for x in range(1000, 10000):
        if x%37==0:
            contador += x
    return contador


def imprimirPiramidesNum():
    contador1 = 0
    contador2 = 0
    for x in range(0,9):
        y = (10 ** x) + contador2
        contador2 = y
        contador1 += contador2
        print(contador1,"* 8", "+", x+1,"=",(contador1 * 8 +(x + 1)))

    contador3 = 0
    for x in range(0, 9):
        z = (10 ** x) + contador3
        contador3 = z
        print(z, "*", z, "=", z ** 2)


def main():
    p = 1
    while p != 0:
        print("""Mision 5. Seleccione que quiere hacer.
            1. Dibujar cuadros y circulos.
            2. Dibujar parábolas.
            3. Dibujar círculos.
            4. Aproximar PI.
            5. Contar divisibles entre 37.
            6. Imprimir pirámides de números.
            0. Salir.""")
        x = int(input("¿Qué desea hacer? "))
        if x > 0 and x < 4:
            dibujar(x)
        elif x == 4:
            y = int(input("Introduzca el ultimo digito o divisor para calcular PI: "))
            if y > 0 and y < 1001:
                a = aproximarPI(y)
                print(a)
            else:
                print("Con ese numero ya no se puede calcular PI.")
        elif x == 5:
            z = calcularDivisibles37()
            print(z)
        elif x == 6:
            print(imprimirPiramidesNum())
        elif x == 0:
            print("Hasta luego.")
        else:
            print("No hay opción con ese número.")


main()