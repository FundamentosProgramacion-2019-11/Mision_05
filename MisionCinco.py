#Autor: Karla Ximena Rueda Ruiz
#Descripción:Este programa despliega un menú de opciones a realizar, referentes a la misión 5.

import math
from random import randint
import pygame

ANCHO = 800
ALTO = 800
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

def dibujaCuadrosyCirculos():

    pygame.init()  # Aqui inicia mi pygame
    ventana=pygame.display.set_mode((ANCHO, ALTO))  #Esto es lo que crea la ventana del dibujo
    reloj=pygame.time.Clock()  #Esto va a hacer que se limiten mis pixeles
    termina = False
    while not termina:

        for c in pygame.event.get():
            if c.type == pygame.QUIT:
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range (1,ANCHO//2,10):

            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1) #circulos
            pygame.draw.rect(ventana,NEGRO,(x,x,ANCHO-x*2,ALTO-x*2),1) #rectangulos

        pygame.display.flip()
        reloj.tick(40)  # Son 40 fps

    pygame.quit()
    main()


def dibujaParabolas():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for p in pygame.event.get():
            if p.type==pygame.QUIT:
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)
        ALEATORIO = randint(0, 255), randint(0, 255), randint(0, 255)
        for x in range (0,ANCHO//2,10):

            pygame.draw.line(ventana,ALEATORIO,(ANCHO//2,ALTO//2+x),(0+x,ALTO//2),1 )
            pygame.draw.line(ventana,ALEATORIO,(ANCHO//2+x,ALTO//2),(ANCHO//2, 0+x),1)
            pygame.draw.line(ventana,ALEATORIO,(0+x,ALTO//2),(ANCHO//2,ALTO//2-x),1)
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2,ALTO//2+x),(ANCHO-x,ALTO//2),1)
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
    main()

def dibujaEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(0,ANCHO//2,10):
            # Aquí haces todos los trazos que requieras
            # Las tres pimeras lineas delimitan lo que son los lados horizontales
            pygame.draw.line(ventana,NEGRO,(ANCHO//2,ALTO//2),(ANCHO//2+10,ALTO//2),1)
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-x,ALTO//2-x),(ANCHO//2+x,ALTO//2-x),1)
            pygame.draw.line(ventana, NEGRO,(ANCHO//2+x+10,ALTO//2+x),(ANCHO//2-x,ALTO//2+x),1)

            #lados verticales

            pygame.draw.line(ventana, NEGRO, (ANCHO//2+10,ALTO//2-10),(ANCHO//2+10,ALTO//2),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO//2-x,ALTO//2+x),(ANCHO//2-x,ALTO//2-x),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO//2+x+10,ALTO//2-x-10),(ANCHO//2+x+10,ALTO//2+x),1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
    main()


def dibujaCirculos():
    #Aqui se van a crear 12 circulos con un radio de 150

    radio=150
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for ci in pygame.event.get():
            if ci.type == pygame.QUIT:
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for angulo in range(0, 360,30):
            anguloRadianes=angulo*math.pi/180 #esto transforma los angulos en radianes
            pygame.draw.circle(ventana,NEGRO,((ANCHO//2+int(radio*math.cos(anguloRadianes)),ALTO//2+int(radio*math.sin(anguloRadianes)))),radio,1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
    main()


def aproximaPi(aprox):

    suma=0
    for valorDenominador in range (1,aprox+1): #con esto se hace el rango para aproximar a pi
        resultadoDivisión=1/valorDenominador**2
        suma+=resultadoDivisión
    porSeis=suma*6
    resultadoAproximado=math.sqrt(porSeis) #sqrt es raiz cuadrada
    print("El valor aproximado de pi es %f"%resultadoAproximado)
    main()



def calculaDivisibles37():

    numerosDivididos=[]
    for numeroDivisible in range(1000,10000):
        if numeroDivisible%37==0:
                numerosDivididos.append(numeroDivisible) #append es para añadir a la lista
    print ("Los números de 4 digitos divisibles entre 37 son ", len(numerosDivididos)) #len es para sacar la longitud de la lista,es decir,cuántos elementos tiene adentro.
    main()


def ImprimirPiramides():

    primerpiramide=0
    num=0

    print()
    for n in range(0,9):
        segundasuma=1+(10**n)
        primerpiramide+=segundasuma-1**n
        num+=primerpiramide
        multiplicacion=num*8+(n + 1)
        print(num,"* 8 +",(n+1),"=",multiplicacion)

    segundapiramide=0
    print()
    for n in range(0,9):
        primersuma= 10 ** n
        segundapiramide +=primersuma
        multiplicacion=segundapiramide*segundapiramide
        print(segundapiramide, "*",segundapiramide,"=",multiplicacion)

    main()







def main():

    variableSeleccion=int(input('''Misión 5.Seleccione qué quiere hacer
    1. Dibujar cuadros y circulos
    2. Dibujar parábolas
    3. Dibujar espiral
    4. Dibujar círculos
    5. Aproximar PI
    6. Contar los numero divisibles entre 37 de 4 numeros
    7. Imprimir piramides de numeros
    0. Salir 
    ¿Qué desea hacer?: '''))
    if variableSeleccion==1:
        dibujaCuadrosyCirculos()
    elif variableSeleccion==2:
        dibujaParabolas()
    elif variableSeleccion==3:
        dibujaEspiral()
    elif variableSeleccion==4:
        dibujaCirculos()

    elif variableSeleccion==5:
        aprox=int(input("¿Hasta qué numero desea aproximar pi?: "))
        aproximaPi(aprox)
    elif variableSeleccion==6:
        calculaDivisibles37()
    elif variableSeleccion==7:
        ImprimirPiramides()
    elif variableSeleccion==0:
        print("Hasta luego")
    else:
        print("Elige una opción viable")
        main()
main()
