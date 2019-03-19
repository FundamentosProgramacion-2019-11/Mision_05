#Yasmín Landaverde Nava
#Descripción: este programa despliega un menú en el que el usuario puede
# elegrir entre ciertos dibujos o ejercicios

import math
import random
import pygame

#medidas de pantalla
ANCHO = 800
ALTO = 800
#colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

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

        for lado in range(0, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (lado, lado, ANCHO - (lado * 2), ANCHO - (lado * 2)), 1)
        for circulo in range(10, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), circulo, 1)
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)
def dibujarLineasEstrella(ventana):
    for y in range(0, 401, 10):
        x = 400 + y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, y), (x, 400))
        for y in range(0, 400, 10):
            x = 400 - y
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (y, 400), (400, x))
            for x in range(0, 401, 10):
                y = 400 + x
                colorAleatorio = generarColor()
                pygame.draw.line(ventana, colorAleatorio, (x, 400), (400, y))
                for y in range(0, 400, 10):
                    x = 800 - y
                    colorAleatorio = generarColor()
                    pygame.draw.line(ventana, colorAleatorio, (400, y + 400), (x, 400))
def dibujarEstrella():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(NEGRO)
        dibujarLineasEstrella(ventana)

        pygame.display.flip()
        reloj.tick(1)

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

        for circulo in range(30, 390, 30):
            angRadianes = math.radians(circulo)
            x = 150 * math.cos(angRadianes)
            y = 150 * math.sin(angRadianes)
            pygame.draw.circle(ventana, NEGRO, (int(x + ANCHO // 2), int(y + ALTO // 2)), 150, 1)
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def aproximarPI(suma):
    division = 0
    for n in range (1, suma+1):
        dividendo = n**-2
        division = division + dividendo
    pi = (division * 6) **(1/2)
    print(pi)

def contarDivisibles():
    total = 0
    for n in range (1000, 10000):
        if n % 37 == 0:
            total += 1
    print (total)

def mostrarPiramide():
    multiplicador = 123456789
    for factor in range (1,10):
        resultado = multiplicador // (10)**(9-factor)
        suma = resultado * 8 + factor
        print(resultado, "x 8 +", factor, "=", suma)
    multiplicador = 111111111
    for factor in range(1, 10):
        resultado = multiplicador // (10) ** (9 - factor)
        suma = resultado * resultado
        print(resultado, "x", resultado, "=", suma)

def main():
    print ("""Misión 5: Selecciona qué quieres hacer: 
1. Dibujar Cuadros y Circulos
2. Dibujar Estrella
3. Dibujar Círculos
4. Aproximar PI
5. Contar divisibles entre 37
6. Imprimir pirámide de números
0. Salir""")
    opcion = int(input("¿Qué desea hacer?: "))
    while opcion>0:
        if opcion == 1:
            dibujarCuadrosCirculos()
            opcion = int(input("¿Qué desea hacer?: "))
        elif opcion == 2:
            dibujarEstrella()
            opcion = int(input("¿Qué desea hacer?: "))
        elif opcion == 3:
            dibujarCirculos()
            opcion = int(input("¿Qué desea hacer?: "))
        elif opcion == 4:
            aproximarPI()
            opcion = int(input("¿Qué desea hacer?: "))
        elif opcion == 5:
            contarDivisibles()
            opcion = int(input("¿Qué desea hacer?: "))
        elif opcion == 6:
            mostrarPiramide()
            opcion = int(input("¿Qué desea hacer?: "))

main()