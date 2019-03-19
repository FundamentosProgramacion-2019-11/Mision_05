#Cecilia Daniela Olivares Hernández, a01745727

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
NEGRO = (0, 0, 0)      # nada de rojo, ni verde, ni azul


#Esta función genera colores aleatorios
def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)


# Esta función dibuja un patron de circulos y cuadrados
def dibujarCuadros(ventana):
    for linea in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (linea, linea, ANCHO - linea * 2, ANCHO - linea * 2), 1)
def dibujarPatronCirculos(ventana):
    for radio in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)

# Esta función dibuja un patron de circulos y cuadrados
def dibujarCirculosyCuadros():
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

        dibujarCuadros(ventana)
        dibujarPatronCirculos(ventana)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    pygame.quit()  # terminar pygame


#Esta función dibuja una estrella con colores aleatorios
def dibujarLineasEstrella(ventana):
    for y in range(0, ALTO // 2, 10):
        xFinal = y + (ANCHO // 2 + 10)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, y), (xFinal, ALTO // 2))
    for y in range(0, ALTO // 2, 10):
        xFinal = -y + (ANCHO // 2 - 10)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, y), (xFinal, ALTO // 2))
    for y in range(0, ALTO // 2, 10):
        xFinal = y + (ALTO // 2 + 10)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (y, ALTO // 2), (ANCHO // 2, xFinal))
    for y in range(0, ALTO // 2, 10):
        xFinal = - y + ANCHO
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, y + ALTO // 2), (xFinal, ALTO // 2))

#Esta función dibuja una estrella con colores aleatorios
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

        dibujarLineasEstrella(ventana)

        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


#Esta función dibuja 12 circulos
def dibujarCirculos(ventana):
    for alfa in range(0, 360, 30):
        angRadianes = math.radians(alfa)
        x = 150 * math.cos(angRadianes)
        y = 150 * math.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(x + ANCHO // 2), int(ALTO // 2 - y)), 150, 1)

#Esta función dibuja 12 circulos
def dibujarDoceCirculos():
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
        reloj.tick(60)
    pygame.quit()


#Esta función calcula una aproximación al valor de PI
def aproximaciónPI(n):
    suma = 0
    for denominador in range(1,n+1):
        operación = 1/(denominador**2)
        suma += operación
    aproximación = ((6*suma)**.5)
    return aproximación


#Esta función calcula los numeros divisibles entre 37
def calcularDivisibles():
    cantidad = 0
    for num in range (1000,10000,1):
        if num% 37 == 0:
            cantidad += 1
    print("La cantidade de números de 4 digitos divisibles entre 37 es:", cantidad)


#Esta función imprime una piramide con digitos del 1 al 9 y otra con unicamente repeticiones del numero 1
def imprimirPiramideDigitos():
    operación = 0
    digito = 0
    for n in range(1 ,10):
        digito = digito*10 + n
        operación = digito * 8 + n
        print(digito, "* 8 +", n,"=", operación)
    print()
    digito = 0
    for n in range(1 ,10):
        digito = digito*10 + 1
        operación = digito *10+1
        print(digito, "*", digito,"=", operación)


#Esta es la función principal que resuelve el problema
def main():
    respuesta = int(input("""Misión 5. Seleccione qué quiere hacer.
    1. Dibujar cuadros y círculos
    2. Dibujar parábolas
    3. Dibujar círculos
    4. Aproximar PI
    5. Contar divisibles entre 37
    6. Imprimir pirámides de números
    0. Salir
    ¿Que desea hacer?"""))
    while respuesta != 0:
        if respuesta == 1:
           dibujarCirculosyCuadros()
        elif respuesta == 2:
            dibujarEstrella()
        elif respuesta == 3:
            dibujarDoceCirculos()
        elif respuesta == 4:
            n = int(input("Inserta un número de divisores: "))
            aproximación = aproximaciónPI(n)
            print("La aproximación al valor de PI es: ", aproximación)
            volver = input("Selecciona enter para regresar al Menu")
        elif respuesta == 5:
            calcularDivisibles()
            volver = input("Selecciona enter para regresar al Menu")
        elif respuesta == 6:
            imprimirPiramideDigitos()
            volver = input("Selecciona enter para regresar al Menu")
        elif respuesta>6 or respuesta<0:
            volver = input("ERROR, Selecciona enter para volver al menu y elige una opción valida")
        respuesta = int(input("""Misión 5. Seleccione qué quiere hacer.
            1. Dibujar cuadros y círculos
            2. Dibujar parábolas
            3. Dibujar círculos
            4. Aproximar PI
            5. Contar divisibles entre 37
            6. Imprimir pirámides de números
            0. Salir
            ¿Que desea hacer?"""))
    if respuesta == 0:
        print("Has decidido Salir de el programa")


# Llamas a la función principal
main()