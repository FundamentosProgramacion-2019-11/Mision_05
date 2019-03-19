# Autor: Roberto Emmanuel González Muñoz A01376803.
# Progama con múltiples funciones.

import pygame
import math
from random import randrange

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
ROSA = (255, 0, 255)
VERDE_POOL = (32, 94, 27)
MORADO = (123, 80, 150)


def menuDeUsuario():
    opcion = int(input(print("________________________________________\n"
                             "Misión 5. Seleccione qué quiere hacer?\n"
                             "1. Dibujar cuadros y círculos.\n"
                             "2. Dibujar estrella.\n"
                             "3. Dibujar espiral.\n"
                             "4. Dibujar círculos.\n"
                             "5. Aproximar Pi.\n"
                             "6. Contar divisibles 37.\n"
                             "7. Imprimir piramides numéricas.\n"
                             "0. Salir.\n"
                             "Qué desea hacer?\n"
                             "________________________________________\n")))
    return opcion


def dibujarCuadradosCirculos():
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

        centro = (ANCHO // 2, ALTO // 2)

        # Dibuja rectángulos en la pantalla
        for delta in range(10, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - delta, ALTO // 2 - delta, 2 * delta, 2 * delta), 1)

        # Dibuja círculos en la pantalla
        for radio in range(10, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, centro, radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


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
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        DELTA = 10

        # Dibuja en 4 sectores una parábola de colores aleatorios.
        for x in range(0, ALTO//2, DELTA):
            pygame.draw.line(ventana, (randrange(0, 255), randrange(0, 255), randrange(0, 255)), (x, ALTO // 2),
                             (ANCHO // 2, x + ALTO // 2))
            pygame.draw.line(ventana, (randrange(0, 255), randrange(0, 255), randrange(0, 255)), (x, ALTO // 2),
                             (ANCHO // 2, ALTO // 2 - x))
            pygame.draw.line(ventana, (randrange(0, 255), randrange(0, 255), randrange(0, 255)), (ANCHO // 2, x),
                            (x + ANCHO // 2, ALTO // 2))
            pygame.draw.line(ventana, (randrange(0, 255), randrange(0, 255), randrange(0, 255)), (ANCHO - x, ALTO // 2),
                             (ANCHO // 2, ALTO // 2 + x))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspiral():
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

        DELTA = 10

        # Lineas horizontales
        for x in range(0, ALTO//2, DELTA):
            pygame.draw.line(ventana, NEGRO, (x, x), (ANCHO + 6 - x, x))
            pygame.draw.line(ventana, NEGRO, (x, x), (x, ALTO + 9 - x))
            pygame.draw.line(ventana, NEGRO, (ANCHO + 6 - x, x), (ANCHO + 6 - x, ALTO - x))
            pygame.draw.line(ventana, NEGRO, (x + 10, ALTO - x), (ANCHO + 6 - x, ALTO - x))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCirulos():
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

        # Dibujar
        radius = 150  # Radio círculo

        # Dibuja un circulo en las coordenadas en donde el radio tiene una separación de 30 grados.
        pygame.draw.circle(ventana, NEGRO, (550, ALTO // 2), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, 250), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (250, ALTO // 2), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, 550), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (475, 270), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (325, 270), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (530, 325), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (270, 325), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (475, 530), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (530, 475), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (270, 475), radius, 1)
        pygame.draw.circle(ventana, NEGRO, (325, 530), radius, 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def aproximacionPi(divisor):
    sumador = 0

    for div in range(1, divisor + 1, 1):
        sumador += (1 / (div ** 2))
    aproximacion = (sumador * 6) ** 0.5

    print("Con %d la apoximación de pi es: %.4f" % (divisor, aproximacion))


def calcularDivisibles37(n):
    if n % 37 == 0 and n != 0:
        print("Es divisible en 37.")
    else:
        print("No es divisible en 37")


def calcularPiramides():
    # Variables contadoras
    c = 1
    a = 0
    z = 0
    b = 1
    k = 0

    # Contador pirámide A
    for x in range(0, 9, 1):
        c = c * 10
        a = a + 1
        z = z * 10 + a
        b = b * 10 + (10 - a)
        print(z, "* 8", "+", a, "=", z * 8 + a)  # Con una cadena el resultado seria (b - c)
    print("_________________________________________________________")

    # Contador pirámide B
    for y in range(0, 9, 1):
        k = (k * 10) + 1
        print(k, "*", k, "=", k * k)


def main():
    # Menu de Usuario y Selección de funciones.
    opcion = 1
    while opcion != 0:
        opcion = menuDeUsuario()

        if opcion == 1:
            dibujarCuadradosCirculos()

        elif opcion == 2:
            dibujarEstrella()

        elif opcion == 3:
            dibujarEspiral()

        elif opcion == 4:
            dibujarCirulos()

        elif opcion == 5:
            divisor = int(input("Teclea el último divisor: "))
            aproximacionPi(divisor)

        elif opcion == 6:
            numero = int(input("Teclea el número que desea calcular: "))
            calcularDivisibles37(numero)

        elif opcion == 7:
            calcularPiramides()

        opcion = menuDeUsuario()

    print("END")


main()
