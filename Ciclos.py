#Autor Sofía Trujillo Vargas
#Resolver ddiferentes ejercicios usando los ciclos for y while, junto con la libreria de Pygame.

import pygame
import math

def main():
    var = -1
    while var != 0:

        print("""
        ¡¡¡BIENVENIDO!!! ESTE ES EL MENÚ
        Misión 5. Seleccione qué quiere hacer.
        1. Dibujar Círculos
        2. Dibujar Espiral
        3. Dibujar Cuadros mezclados con Círculos
        4. Aproximación de PI
        5. Divisibles enre 37
        6. Piramide de Cadena""")

        var = int(input("¿Qué desea hacer?"))

        if var == 1:
            dibujarCirculos()

        elif var == 2:
            dibujarEspiral()

        elif var == 3:
            dibujarCuadradosYCirculos()

        elif var == 4:
            divisor = int(input("Teclee el valor del último divisor: "))
            pi = aproxPi(divisor)
            print(pi)
            pausa = input("Int para ver más opciones")

        elif var == 5:
            ncou = numerosDivis37()
            print("Total de números divisibles entre 37 es: ",numerosDivis37())
            pausa = input("Int para ver más opciones")

        elif var == 6:
            imprimirPiramide()

        elif var == 0:
            print("BUEN DÍA ")

        else:
            print("Valor invalido, incerte valor dentro del menú")
            pausa = input("Int para ver más opciones")



BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

ANCHO = 800
ALTO = 800

def dibujarCirculos():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False

    while not end:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True


        ventana.fill(BLANCO)

        r = 150
        a = 30

        for circulos in range(1, 13):
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(r * math.cos(math.radians(a * circulos)))),
            (ALTO // 2) + (int(r * math.sin(math.radians(a * circulos))))), r, 1)

        pygame.display.flip()
        reloj.tick(100)


    pygame.quit()

def dibujarEspiral():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True

        ventana.fill(BLANCO)

        for posicion in range(10, ALTO//2, 10):
            pygame.draw.line(ventana, NEGRO, ((ANCHO + 5) - posicion, ALTO - posicion), (0 + posicion, ALTO - posicion), 1)
            pygame.draw.line(ventana, NEGRO, (0 + posicion, ALTO - posicion), (0 + posicion, 0 + posicion), 1)
            pygame.draw.line(ventana, NEGRO, (0 + posicion, 0 + posicion), (ANCHO - (posicion), 0 + posicion), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - posicion, 0 + posicion), (ANCHO - posicion, ALTO - (posicion + 10)), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - posicion, ALTO - (posicion + 10)), ((ANCHO - 7) - posicion, ALTO - (posicion + 10)), 1)

        pygame.display.flip()
        reloj.tick(100)

    pygame.quit()

def dibujarCuadradosYCirculos():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True

        ventana.fill(BLANCO)

        for rect in range(2, ALTO, 20):
            pygame.draw.rect(ventana, NEGRO, [(ANCHO // 2 - rect // 2), (ALTO // 2 - rect // 2), rect, rect], 1)

        for radio in range(1, ALTO//2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2) , radio, 1)

        pygame.display.flip()
        reloj.tick(100)

    pygame.quit()

def aproxPi(n):
    suma = 0

    if n<=0:
        print("Numero invalido.")

    else:
        for d in range(1, n + 1):
            fracción = 1 / d ** 2
            suma += fracción

    aproxPi = (6 * suma) ** 0.5
    return aproxPi

def numerosDivis37():
    ncou = 0
    for n in range (1000,9999):
        if n % 37 == 0:
            ncou = ncou + 1
        else:
            pass
    return ncou

def imprimirPiramide():
    num = 8
    for x in range(0, 9):
        string = int(round((10**x+2*10**(x-1)+3*10**(x-2)+4*10**(x-3)+5*10**(x-4)+6*10**(x-5)+7*10**(x-6)+8*10**(x-7)+9*10**(x-8)),1))
        r = string * num + (x+1)
        print("{} * {} + {} = {}".format(string, num, x, r))
    pausa = input("Int Continuar")

    for z in range(0, 9):
        string2 = int(round((10 ** z + 1 * 10 ** (z - 1) + 1 * 10 ** (z - 2) + 1 * 10 ** (z - 3) + 1 * 10 ** (z - 4) + 1 * 10 ** (z - 5) + 1 * 10 ** (z - 6) + 1 * 10 ** (z - 7) + 1 * 10 ** (z - 8)), 1))
        r = string2 * string2
        print("{} * {} = {}".format(string2, string2, r))
    pausa = input("Int continuar")


main()