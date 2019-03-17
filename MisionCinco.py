#Bruno Omar Jimenez Mancilla
#Un programa que despliega un menu y permite hacer diferentes figuras y funciones como hacer una aproximacipon de pi entre otras

import pygame
import random
import math
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

def imprimirPiramides():
    num = 8
    for i in range(0, 9):
        secuencia = int(round((10 ** i + 2 * 10 ** (i - 1) + 3 * 10 ** (i - 2) + 4 * 10 ** (i - 3) + 5 * 10 ** (
                    i - 4) + 6 * 10 ** (i - 5) + 7 * 10 ** (i - 6) + 8 * 10 ** (i - 7) + 9 * 10 ** (i - 8)), 1))
        resultado = secuencia * num + (i + 1)
        print(secuencia,"*", num ,"+", i,"=", resultado)
    pausa = input("Pulsa cualquier tecla para continuar") #Se utiliza para visualizar el resultado mas facilmente
    for j in range(0, 9):
        secuencia = int(round((10 ** j + 1 * 10 ** (j - 1) + 1 * 10 ** (j - 2) + 1 * 10 ** (j - 3) + 1 * 10 ** (
                    j - 4) + 1 * 10 ** (j - 5) + 1 * 10 ** (j - 6) + 1 * 10 ** (j - 7) + 1 * 10 ** (j - 8)), 1))
        resultado = secuencia * secuencia
        print(secuencia,"*", secuencia,"=", resultado)
    pausa = input("Pulsa cualquier tecla para regresar al menú")


def dibujarEspiral():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(10, ALTO//2, 10):
            pygame.draw.line(ventana, NEGRO, ((ANCHO + 10) - x, ALTO - x), (0 + x, ALTO - x), 1)
            pygame.draw.line(ventana, NEGRO, (0 + x, ALTO - x), (0 + x, 0 + x), 1)
            pygame.draw.line(ventana, NEGRO, (0 + x, 0 + x), (ANCHO - (x), 0 + x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - x, 0 + x), (ANCHO - x, ALTO - (x + 10)), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - x, ALTO - (x + 10)), ((ANCHO - 7) - x, ALTO - (x + 10)), 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps


    pygame.quit()  # terminar pygame


def dibujarDoceCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        radio = 150
        alfa = 30

        for circulos in range(1, 13):
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(radio * math.cos(math.radians(alfa * circulos)))),
            (ALTO // 2) + (int(radio * math.sin(math.radians(alfa * circulos))))), radio, 1)

        pygame.display.flip()
        reloj.tick(60)


    pygame.quit()


def dibujarCuadradosYCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for lrect in range(2, ALTO, 10):
            pygame.draw.rect(ventana, NEGRO, [(ANCHO // 2 - lrect // 2), (ALTO // 2 - lrect // 2), lrect, lrect], 1)

        for radio in range(1, ALTO//2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2) , radio, 1)

        pygame.display.flip()
        reloj.tick(60)


    pygame.quit()

def aproximarPI(n):
    suma = 0
    for d in range(1,n+1):
        fraccion = 1/(d**2)
        suma += fraccion
    aproximacionPi = (6*suma) ** 0.5
    return aproximacionPi

def contarDivisibles():
    numeroCont = 0

    for numeros in range(1000, 10000, 1):
        if numeros % 37 == 0:
            numeroCont = numeroCont + 1
        else:
            pass
    return numeroCont


def main():
    menu = 0
    while menu != 7:
        print("Misión 5. Seleccione qué quiere hacer.")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar espiral")
        print("3. Dibujar círculos")
        print("4. Aproximar PI")
        print("5. Contar números divisibles entre 37 de cuatro dígitos")
        print("6. Imprimir pirámides de números")
        print("7. Salir")
        menu = int(input("¿Qué desea hacer?"))
        if menu == 1:
            dibujarCuadradosYCirculos()
        if menu== 2:
            dibujarEspiral()
        if menu == 3:
            dibujarDoceCirculos()
        if menu == 4:
            n = int(input("Teclea el número de divisores: "))
            pi = aproximarPI(n)
            print("La aproximación de pi es:  ",pi)
            pausa = input("Pulsa cualquier tecla para regresar al menú")

        if menu == 5:
            div = contarDivisibles()
            print("Números de cuatro dígitos divisibles entre 37: ",div)
            pausa = input("Pulsa cualquier tecla para regresar al menú")

        if menu == 6:
            imprimirPiramides()


        if menu == 7:
            print("Adiós")

        else:
            print("Error: indique un valor correcto.")
            pausa = input("Presione enter para continuar...")



main()
