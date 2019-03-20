# Karimn Daniel Hernández Castorena
# Programa que permite dibujar figuras y realizar diferentes operaciones.

import pygame
import random
import math

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


# Dibujar Estrella
def generarColorAzar():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo, verde, azul)
    return colorX


def dibujarLineasEstrella(ventana):
    for y in range(0, ALTO // 2 + 1, 10):
        colorRandom = generarColorAzar()
        pygame.draw.line(ventana, colorRandom, (0 + y, ALTO // 2), (ANCHO // 2, ALTO // 2 - y))
    for y in range(0, ANCHO // 2 + 1, 10):
        colorRandom = generarColorAzar()
        pygame.draw.line(ventana, colorRandom, (ANCHO - y, ALTO // 2), (ANCHO // 2, ALTO // 2 + y))
    for y in range(0, ALTO // 2 + 1, 10):
        colorRandom = generarColorAzar()
        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, ALTO // 2 - y), (ANCHO - y, ALTO // 2))
    for y in range(0, ALTO // 2 + 1, 10):
        xFin = y + 10
        colorRandom = generarColorAzar()
        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, ALTO // 2 + y), (0 + y, ALTO // 2))


def dibujarFiguraEstrella():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        dibujarLineasEstrella(ventana)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()


# DibujarCírculos
def dibujarLineasCirculos(ventana):
    for alfa in range(30, 390, 30):
        angRad = math.radians(alfa)
        x = 150 * math.cos(angRad)
        y = 150 * math.sin(angRad)
        pygame.draw.circle(ventana, NEGRO, (int(x + ANCHO // 2), int(ALTO // 2 - y)), 150, 1)


def dibujarFigurasCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        dibujarLineasCirculos(ventana)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()


# Dibujar Cuadrados con círculos
def dibujarLineasCuadradosyCirculos(ventana):
    for r in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), r, 1)

    for l in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (l, l, ANCHO - (l * 2), ALTO - l * 2), 1)


def dibujarCuadradosyCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        dibujarLineasCuadradosyCirculos(ventana)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()


# Pi
def calcularPiProximo(num):
    sum = 0
    for d in range(1, num + 1):
        f = 1 / (d ** 2)
        sum += f

    pi = (sum * 6) ** 0.5
    return pi


# Numeros
def calcularNumeros4a37():
    cn = 0
    for n in range(1000, 10000):
        if n % 37 == 0:
            cn += 1
    return cn


# Operaciones
def calcularOperaciones():
    op1 = 0
    for num1 in range(1, 10):
        op1 = op1 * 10 + num1
        res1 = op1 * 8 + num1
        print(op1, "*8  + ", num1, "=", res1)
    print()
    op2 = 0
    for dig in range(1, 10):
        op2 = op2 * 10 + 1
        res2 = op2 * op2
        print(op2, "*", op2, "=", res2)
    print()


def main():
    print()
    print("Hola usuario :D")
    print()
    print("¿Qué es lo que deseas hacer?")
    print()
    print("1.- Dibujar estrella de colores.")
    print("2.- Dibujar círculos.")
    print("3.- Dibujar una espiral con un cuadrado detrás")
    print("4.- Aproximar el valor de PI")
    print("5.- Contar números divisibles entre 19")
    print("6.- Crear un pirámide de números")
    print()
    print("0.- Salir")
    print()

    decision = 100
    while decision != 0:
        decision = int(input("Escribe el número de lo que desea hacer: "))
        print()
        if decision == 1:
            dibujarFiguraEstrella()
        if decision == 2:
            dibujarFigurasCirculos()
        if decision == 3:
            dibujarCuadradosyCirculos()
        if decision == 4:
            num = int(input("Introduce un número para aproximar: "))
            print()
            calcularPiProximo(num)
            pi = calcularPiProximo(num)
            print("El número es:", pi)
            print()
        if decision == 5:
            calcularNumeros4a37()
            num = calcularNumeros4a37()
            cn = calcularNumeros4a37()
            print("La cantidad de números divisibles es de:", cn)
            print()
        if decision == 6:
            calcularOperaciones()
        elif decision < 0 or decision > 6:
            print("¿Qué te pasa?")
            print("Decisión invalida >:(")
            print()
    print("Adiós usuario! Que la Fuerza te acompañe!")


main()
