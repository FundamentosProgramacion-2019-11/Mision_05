import pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

def dibujarCirculos(ventana):
    alfa = 0
    while alfa<390:
        alfa += 30
        x = 150 * math.cos(math.radians(alfa))
        y = 150 * math.sin(math.radians(alfa))
        pygame.draw.circle(ventana, ROJO, (int(x) + ANCHO//2, int(y) + ANCHO//2), 150, 1)


def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def dibujarCuadrosCirculos(ventana):
    y = 0
    while y<400:
        y += 10
        pygame.draw.rect(ventana, AZUL, (y, y, 800-(y*2), 800-(y*2)), 1)

    radio = 0
    while radio<400:
        radio += 10
        pygame.draw.circle(ventana, AZUL, (400,400), radio, 1)


def dibujar2():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarCuadrosCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def generarColorAzar():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorx = (rojo,verde,azul)
    return colorx

def dibujarArco(ventana):
    for x in range(10, ANCHO//2+1, 10):
        y = ALTO//2-x+10
        x2 = y + 410
        x3 = 800 - y
        colorAzar = generarColorAzar()
        pygame.draw.line(ventana, colorAzar, (x,400), (400,y))
        pygame.draw.line(ventana, colorAzar, (y,400), (400,x2))
        pygame.draw.line(ventana, colorAzar, (x2,400), (400,y))
        pygame.draw.line(ventana, colorAzar, (400,y+400), (x3,400))

def dibujar3():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarArco(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def aproximarPI(n):
    suma = 0
    for d in range(1, n+1):
        fraccion = 1/d**2
        suma += fraccion

    suma = suma*6
    aproxPI = suma**0.5
    print(aproxPI)

def operacion1():
    for n in range(1, 123456790):
        if n == 1:
            operacion1 = n * 8 + 1
            print(operacion1)
        elif n == 12:
            operacion1 = n * 8 + 2
            print(operacion1)
        elif n == 123:
            operacion1 = n * 8 + 3
            print(operacion1)
        elif n == 1234:
             operacion1 = n * 8 + 4
             print(operacion1)
        elif n == 12345:
            operacion1 = n * 8 + 5
            print(operacion1)
        elif n == 123456:
            operacion1 = n * 8 + 6
            print(operacion1)
        elif n == 1234567:
            operacion1 = n * 8 + 7
            print(operacion1)
        elif n == 12345678:
            operacion1 = n * 8 + 8
            print(operacion1)
        elif n == 123456789:
            operacion1 = n * 8 + 9
            print(operacion1)

def operacion2():
    for n in range(1, 111111112):
       if n == 1 or n == 11 or n == 111 or n == 1111 or n == 11111 or n == 111111 or n == 1111111 or n == 11111111 or n== 111111111:
           operacion2 = n*n
           print(operacion2)

def seleccion():
    opcion = str(input("Elija la función que desea ejecutar (opciones A (Dibujar círculos), B(Dibujar cuadros y círculos), C(Dibujar estrella), D(Aproximar un número a Pi), E(Imprimir piramides de números), F(Exit): "))
    if opcion == "A":
        return dibujar()
    elif opcion == "B":
        return dibujar2()
    elif opcion == "C":
        return dibujar3()
    elif opcion == "D":
        return aproximarPI()
    elif opcion == "E":
        return operacion1() and operacion2()
    elif opcion == "F":
        exit()
    else:
        return seleccion()


def main():
    seleccion()

main()