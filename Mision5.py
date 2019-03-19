#Autor: Luis Alberto Zepeda Hernandez
#Comentarios: crear prgrama con menú y que tenga distintas funciones.

import random
import math
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)

#Funcion para generar colores aleatorios.
def generarColor():
    rojo = random.randint(0,225)
    verde = random.randint(0,225)
    azul = random.randint(0,225)
    return(rojo,verde,azul)


#Funcion para dibujar estrella.
def dibujarLineasEstrellas (ventana):
    for y in range(0, 401,10):
        x = y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(400,y),(400+x,400))
    for y2 in range(0, 401,10):
        x2 = y2 +10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(400,y2),(400 -x2,400))
    for y3 in range(0, 401,10):
        x3 = y3
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(400,800-x3),(400-x3,400))
    for y4 in range(0, 401, 10):
        x4 = y4 + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (400, 800 - x4), (400 + x4, 400))
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
        dibujarLineasEstrellas(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(5)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Funcion para dibujar CuadrosCirculos.
def dibujarCuadrosConCirculos(ventana):

    for separacion in range (10,410,10):
        pygame.draw.rect(ventana,NEGRO,(400-separacion,400-separacion,separacion*2,separacion*2),1)


    for radio in range(10,400,10):
        pygame.draw.circle(ventana,NEGRO,(400,400),radio,1)
def dibujarBOXCircle():
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(BLANCO)
        dibujarCuadrosConCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(5)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Funcion para dibujar DoceCirculos.
def dibujarDoceCirculos(ventana):
    for alfa in range (30,361,30):
        angRadiandes = math.radians(alfa)
        x = 150*math.cos(angRadiandes)
        y = 150*math.sin(angRadiandes)
        pygame.draw.circle(ventana,NEGRO, (int(x+400),int(400-y)),150,1)
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

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(5)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Funcion para calcular la aproximación de pi.
def aproximarPi(ultimoDivisor):
    suma = 0
    for divisor in range(1, ultimoDivisor + 1):
        fraccion = 1/(divisor**2)
        suma += fraccion

    aproxPI = (suma*6)**.5
    return aproxPI


#Funcion divisibles entre 37
def divideEntre37():
    suma = 0
    for digitos in range (1000,10000):
        if digitos % 37 == 0:
            suma += 1

    print( "Números divisibles entre 37= " ,suma)


#Funcion pirámide de números
def piramideDeNumeros():
    multi =0
    for suma in range (1,10):
        multi = multi*10+suma
        total = multi * 8 + suma
        print(multi, "* 8 +",suma,"=",total)

    print()
    print()

    multi2=0
    for iteraciones in range(1,10):
        multi2 = multi2*10+1
        total2 = multi2 * multi2
        print(multi2,"*",multi2, "=",total2)



def main():

    print("Misión 5. Seleccione que hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas" )
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar pi")
    print("6. Contar divisibles entre 37")
    print("7. Imprimir pirámides de números")
    print("0. Sailr")

    eleccion = int(input("¿Qué desea hacer? "))

    while eleccion != 0:

        if eleccion == 1:
            dibujarBOXCircle()
        elif eleccion == 2:
            dibujarEstrella()
        elif eleccion == 3:
            print ("Programa no realizado")
        elif eleccion == 4:
            dibujarCirculos()
        elif eleccion == 5:
            ultimoDivisor = int(input("Ingresa número de divisores: "))
            pi = aproximarPi(ultimoDivisor)
            print("El aproximado es: ",pi)
        elif eleccion == 6:
            divideEntre37()
        elif eleccion == 7:
            piramideDeNumeros()
        print()
        print()
        eleccion = int(input("¿Qué desea hacer? "))


    print("programa terminado")





main()



