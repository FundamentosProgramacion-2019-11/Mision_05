#Autor: Katia Hernández Barrera
#Programa que ejecuta diversas acciones que el usuario elige a traves de un menú

import math
import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0) #ausencia de color

def dibujarCuadrosCirculos(ventana):
    for radio in range (10,400, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

    for rect in range (10, 400, 10):
        pygame.draw.rect(ventana, NEGRO, (rect, rect, ANCHO-(rect*2), ALTO-rect*2),1)

def dibujarCuadroyCirc():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj= pygame.time.Clock()
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


def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)


def dibujarLineasEstrella(ventana):
    for y in range(0, ALTO//2, 10):
        xFinal = y + (400 +10)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y), (xFinal, 400))

    for y in range(0, ALTO//2, 10):
        xFinal = -y +(390)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y), (xFinal, 400))

    for y in range(0, ALTO//2, 10):
        xFinal = y + (400 + 10)
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (y, 400), (400, xFinal))

    for y in range(0, ANCHO//2, 10):
        xFinal = -y + ANCHO
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y + 400), (xFinal, 400))


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

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(20)  # 40 fps

    # Después del ciclo principal
    pygame.quit()

def dibujarDoceCirculos(ventana):
    for alfa in range(0,360,30):
        angRadianes = math.radians(alfa)
        x = 150 * math.cos(angRadianes)
        y = 150 * math.sin(angRadianes)
        pygame.draw.circle(ventana,NEGRO,(int(x + ANCHO//2),int(ALTO//2- y)),150,1)

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
        dibujarDoceCirculos(ventana)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def calcularCantidadDivisibles():
    divisibles37 = 0
    for n in range(1000, 10000):
        if n%37 == 0:
            divisibles37+=1
    return divisibles37

def calcularOperaciones():
    operacion = 0
    producto = 0
    for n in range(0,10):
        operacion = operacion*10 + n
        r = (operacion)*8 + n
        print(operacion,"*8 +",n,"=", r)
    print("--------------------------")
    for numero in range (0,9):
        producto = producto *10 +1
        r2 = producto**2
        print(producto,"*",producto,"=",r2)

        
def aproximarPI(pI):
    suma = 0
    for d in range(1, pI+1):
        fraccion = 1/d**2
        suma += fraccion
    aproxPI = math.sqrt(suma*6)
    return aproxPI

def main():
    print("Bienvenido a Misión 5, elige una de las siguientes opciones")
    print("1. Dibujar círculos y cuadros")
    print("2. Dibujar estrella")
    print("3. Dibujar círculos")
    print("4. Aproximar PI")
    print("5. Contar números de cuatro dígitos divisibles entre 37")
    print("6. Imprimir pirámides de números")
    print("7. Salir")
    opcion = int(input("seleccione una opción"))
    while opcion >= 0 and opcion <= 7:
        if opcion == 1:
            dibujarCuadroyCirc()
        elif opcion == 2:
            dibujarEstrella()
        elif opcion == 3:
            dibujarCirculos()
        elif opcion == 4:
            pI = int(input("número: "))
            aproxPi = aproximarPI(pI)
            print("PI = ", aproxPi)
        elif opcion == 5:
            divisibles = calcularCantidadDivisibles()
            print("La cantidad de números de cuatro dígitos divisibles entre 37 es: ", divisibles)
        elif opcion == 6:
            calcularOperaciones()
        elif opcion == 7:
            print("Adiós")
        print("                                                        ")
        print("Bienvenido a Misión 5, elige una de las siguientes opciones")
        print("1. Dibujar círculos y cuadros")
        print("2. Dibujar estrella")
        print("3. Dibujar círculos")
        print("4. Aproximar PI")
        print("5. Contar números de cuatro dígitos divisibles entre 37")
        print("6. Imprimir pirámides de números")
        print("7. Salir")
        opcion = int(input("seleccione una opción"))


main()