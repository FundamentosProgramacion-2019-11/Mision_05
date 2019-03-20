# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Programa el cual por medio de un menu realiza distintas opciones dependiendo de lo que seleccione el usuario


import pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)

def generarColorAzar():
    rojo = random.randint(0,255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo,verde,azul)
    return colorX


def aproximarPI(n):
    suma = 0
    for d in range(1, n+1):
        fraccion = 1 / d**2
        suma += fraccion
    suma = suma*6
    aproxPi = suma ** 0.5
    return aproxPi


def contarDiv37(n):
    contadorDiv = 0
    for pd in range(37, 10000, 37):
        if n % pd == 0:
            contadorDiv += 1
    if contadorDiv == 2:
        return True
    else:
        return False


def imprimirPiramides():
    a=1
    b=0
    c=0
    d=1
    e=0
    for x in range(0,9,1):
        a=a+10
        b=b+1
        c=c*10+b
        d=d*10+(10-a)
        print(c,"*8","+",b,"=",c*0+b)

    for y in range(0,9,1):
        e=(e*10)+1
        print(e,"*",e,"=",e*e)


def dibujarCuadrosCirculos():
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

        pC=(ANCHO//2,ALTO//2)

        for c in range(10,ALTO//2,10):
            pygame.draw.rect(ventana,NEGRO,(400-c,400-c,2*c,2*c),1)
        for pp in range (10,ALTO//2,10):
            pygame.draw.circle(ventana, NEGRO, pC, pp, 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarParabola(ventana):
    for x in range(10, ANCHO//2+ 1, 10):
        y = ALTO//2- x - 10
        color=generarColorAzar()
        pygame.draw.line(ventana, color, (x,400),(400,y))


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
        dibujarParabola(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(5)  # 5 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def cirrculos(ventana):
    pygame.draw.circle(ventana, NEGRO, (550,ALTO // 2 ), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (ANCHO//2, 250), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (250, ALTO // 2), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (ANCHO//2, 550), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (475,270), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (325, 270), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (530, 325), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (270,325), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (475,530), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (530,475), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (270, 475), 150, 1)
    pygame.draw.circle(ventana, NEGRO, (325, 530), 150, 1)


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
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        cirrculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    print("Misión 5. Seleccione qué quiere hacer.\n1.Dibujar cuadros y círculos\n2.Dibujar parábolas\n3.Dibujar círculos\n4.Aproximar PI\n5.Contar divisibles entre 37\n6.Imprimir piramides de números\n0.Salir")
    seleccion = int(input("Seleccion: "))
    while seleccion != 0:
        if seleccion == 1:#cuadros circulos
            dibujarCuadrosCirculos()
        elif seleccion == 2:#estrella
            dibujarEstrella()
        elif seleccion == 3:#circulos
            dibujarCirculos()
        elif seleccion == 4:#aproximarpi
            n=int(input("Teclea el valor el cual quieres aproximar PI: "))
            print(aproximarPI(n))
        elif seleccion == 5:#div37
            for pp in range (1000,10000):
                contarDiv37(pp)
                if contarDiv37(pp) == True:
                    print(pp)
        elif seleccion == 6:#piramides
            print(imprimirPiramides())
        print("Misión 5. Seleccione qué quiere hacer.\n1.Dibujar cuadros y círculos\n2.Dibujar parábolas\n3.Dibujar círculos\n4.Aproximar PI\n5.Contar divisibles entre 37\n6.Imprimir piramides de números\n0.Salir")
        seleccion = int(input("Seleccion: "))


main()