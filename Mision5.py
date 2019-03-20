# Autor: Itzel Yanabany Castro Becerril
# Crear un programa que le muestre al usuario opciones las cuales el podra ver

import math
import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)# nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)

# Estructura básica de un programa que usa pygame para dibujar



def dibujarCirculos(ventana):
    for x in range(10 ,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2,ALTO//2), x,1)
        pygame.draw.rect(ventana,NEGRO, (ANCHO//2-x,ALTO//2-x,x*2, x*2),1)


def dibujarCuadrosYcirculos():
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
        # dibujarCirculos(ventana)
        dibujarCuadrados(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame





def dibujarCuadrados(ventana):
    for x in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1)
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x, x * 2, x * 2), 1)


def dibujar():
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

        #dubujarCuadrado(ventana)
        dibujarCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema

def dibujarDoceCirculoa(ventana):
    for z in range (1,360,30):
        alfa=z
        angRadianes=math.radians(alfa)
        x=150*math.cos(angRadianes)
        y=150*math.sin(angRadianes)
        pygame.draw.circle(ventana,NEGRO,(int(x+ALTO//2),int(ALTO//2-y)),150,1)




def dibujarCirculos():
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
        dibujarDoceCirculoa(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja

def generarColor():
    rojo=random.randint(0,255)
    verde=random.randint(0,255)
    azul=random.randint(0,255)

    return (rojo,verde,azul)


def dibujarEstrella1(ventana):
    for x in range(400, ANCHO + 1, 10):
        y = x - 410
        colorAlazar = generarColor()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))

def dibujarEstrella2(ventana):
    for x in range(0, 400 + 1, 10):
        y = 400 - x
        colorAlazar = generarColor()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))

def dibujarEstrella3(ventana):
    for x in range(0, 400 + 1, 10):
        y = 400 + x
        colorAlazar = generarColor()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))

def dibujarEstrella4(ventana):
    for x in range(400, ANCHO + 1, 10):
        y = ALTO - x + 400
        colorAlazar = generarColor()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))


def dibujarParabola():
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
        dibujarEstrella1(ventana)
        dibujarEstrella2(ventana)
        dibujarEstrella3(ventana)
        dibujarEstrella4(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def dibujar():
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
       #dubujar circulo con toda la informacion



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def esDivisible37():
    suma = 0
    for n in range(1000, 9999):
        if n%37==0:
            suma+= 1
    return suma

def aproximarPI(n):
    suma = 0
    for d in range(1, n + 1):  # 1,2,3...,n
        fraccion = 1 / d ** 2
        suma += fraccion
    aproPi = (6 * suma) ** 0.5
    return aproPi


def piramides():
    n = 0
    for x in range(1, 10):
        n = n * 10 + x
        o = n * 8 + x
        print(n, "* 8 +", x, "=", o)
    m = 0
    for y in range(1, 10):
        m = m * 10 + 1
        v = m * m
        print(m, "*", m, "=", v)



def main():
    print("""Misión 5. Seleccione qué quiere hacer.
1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar círculos
4. Aproximar PI
5. Contar divisibles entre 37
6. Imprimir pirámides de números
0. Salir""")
    r = int(input("¿Qué desea hacer?: "))
    while r >=0 and r<=6:
        if r==1:
            dibujarCuadrosYcirculos()
            r = int(input("¿Qué desea hacer?: "))

        if r==2:
            dibujarParabola()
            r = int(input("¿Qué desea hacer?: "))
        if r==3:
            dibujarCirculos()
            r = int(input("¿Qué desea hacer?: "))
        if r == 4:
            print("El valor aproximado de Pi es de: ",aproximarPI(1000))
            r = int(input("¿Qué desea hacer?: "))
        if r == 5:
            print("La cantidad de numeros de 4 digitos divisibles en 37 son : ",esDivisible37())
            r = int(input("¿Qué desea hacer?: "))
        if r == 6:
            print( piramides())
            r = int(input("¿Qué desea hacer?: "))

        if r == 0:
            print("""Misión 5. Seleccione qué quiere hacer.
            1. Dibujar cuadros y círculos
            2. Dibujar parábolas
            3. Dibujar círculos
            4. Aproximar PI
            5. Contar divisibles entre 37
            6. Imprimir pirámides de números
            0. Salir""")
            r = int(input("¿Qué desea hacer?: "))



main()


