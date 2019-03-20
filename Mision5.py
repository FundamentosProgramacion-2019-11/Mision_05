# encoding: UTF-8
# Autor: Diego Raul Elizalde Uriarte
# Tarea de la Mision 5

import pygame   # Librería de pygame
import random as r
import math as m
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)         #nada de rojo, ni verde, ni azul

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(radio,x,y):
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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        #pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO-60, ALTO-60), 3)
        #dibujarCirculo(ventana,radionx,y)
        pygame.draw.circle(ventana, ROJO, (x, y), radio)
        #pygame.draw.line(ventana, AZUL, (0, ALTO//2), (ANCHO, ALTO//2))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def generarColor():
    ROJO = r.randint(0,255)
    VERDE = r.randint(0,255)
    AZUL = r.randint(0,255)
    return (ROJO,VERDE,AZUL)



def dibujarLineasEstrella(ventana):
    for y in range (0,ALTO//2,10):
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio,(ANCHO//2, y), (ANCHO//2 + y, ALTO//2))
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, y), (ANCHO // 2 - y, ALTO // 2))


    for x in range(0, ANCHO // 2, +10):
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))


    for x in range(ANCHO // 2, ANCHO, +10):
        colorAleatorio = generarColor()
        y = ALTO - x + 10
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, y + ALTO//2), (x, ALTO // 2))





def dibujarDoceCirculos(ventana):
    for alfa in range (0,360,30):
        anguloRadianes = m.radians(alfa)
        x = 150 * m.cos(anguloRadianes)
        y = 150 * m.sin(anguloRadianes)
        pygame.draw.circle(ventana,NEGRO,(int(x + ANCHO//2), int(ALTO//2 - y)),150,1)



def dibujarCirculos(ventana):
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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarDoceCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEstrella(ventana):
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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarLineasEstrella(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCuadrados(ventana):
    lado = 10
    for x in range(5, ALTO, 10):
        pygame.draw.rect(ventana, NEGRO, [ANCHO // 2 - x, ALTO // 2 - x, lado, lado], 1)
        lado += 20

    for r in range(10, ALTO // 2, 5):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), r, 1)



def dibujarCuadrosCirculos(ventana):
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
        # dibujarCuadricula(ventana)

        dibujarCuadrados(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspiral(ventana):
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
        # dibujarCuadricula(ventana)

        dibujarLineas(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def ContarDivisibles(n):
    return n % 37 == 0


def aproximarPi(n):
    suma = 0
    for  d in range(1, n+1):
        fraccion = 1 / d**2
        suma = suma + fraccion   # se puede escribir como: suma += fraccion

    aproxPi = (6*suma) **0.5
    return aproxPi



def formarPiramide():
    b = 0
    c = 0
    for diferencial in range (0,9,1):
        base = 10**diferencial
        b += base
        c += b
        num = diferencial + 1
        rFinal = c*8 + num
        print(c,"* 8 +", num, "=", rFinal)
    print( )
    cont = 0
    for num in range(0,9,1):
        Base = 10**num
        cont += Base
        piramide = cont**2
        print(cont, "*", cont, "=", piramide)

def dibujarLineas(ventana):
    for x in range(1,400,10):
        pygame.draw.line(ventana, NEGRO, (405 + x, 390 - x), (390 - x, 390 - x),1)
        pygame.draw.line(ventana, NEGRO, (390 - x, 390 - x), (390 - x, 410 + x),1)
        pygame.draw.line(ventana, NEGRO, (400 - x, 400 + x), (405 + x, 400 + x),1)
        pygame.draw.line(ventana, NEGRO, (405 + x, 400 + x), (405 + x, 390 - x),1)


def main():
    print("""Mision 5. Seleccione que quiere hacer 
              1. Dibujar cuadros y circulos
              2. Dibujar parabolas
              3. Dibujar espiral
              4. Dibujar circulos
              5. Aproximar PI
              6. Contar divisibles entre 37
              7. Imprimir piramide de numeros
              0. Salir""")
    mision5 = input("Que numero deseas realizar?")
    while mision5 != "0":
        if mision5 == "1":
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            dibujarCuadrosCirculos(ventana)
        elif mision5 == "2":
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            dibujarEstrella(ventana)
        elif mision5 == "3":
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            dibujarEspiral(ventana)
        elif mision5 == "4":
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            dibujarCirculos(ventana)
        elif mision5 == "5":
            n = int(input("¿Hasta que número quieres hacer tu aproximación?"))
            PIA = aproximarPi(n)
            print(PIA)
        elif mision5 == "6":
            Divisibles = 0
            for n in range(1, 10000):
                if ContarDivisibles(n):
                    Divisibles += 1
                else:
                    Divisibles += 0
            print("El total de divisibles es: ", Divisibles)

        elif mision5 == "7":
            formarPiramide()
        mision5 = input("Que numero deseas realizar?")




# Llamas a la función principal
main()