#Yadira Fuentes Calderón A01745235
#Programa que realiza distintas selecciones dependiendo de lo que el usuario pida

import pygame
import random
import math

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)


#---------------------------------DibujarCuadradosCirculos-----------------------------
def dibujarLineasCuadradosCirculos(ventana):
    for radio in range (10,ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

    for lado in range (10, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (lado, lado, ANCHO-(lado*2), ALTO-lado*2),1)

def dibujarCuadradosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj= pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        dibujarLineasCuadradosCirculos(ventana)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
#---------------------------------------------------------------------------------------


#---------------------------------DibujarEstrella---------------------------------------
def generarColor():
    rojo= random.randint(0,255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)

def dibujarLineasEstrella(ventana):
    for y in range (0, ALTO//2+1, 10):
        color= generarColor()
        pygame.draw.line(ventana, color, (0+y, ALTO//2), (ANCHO//2, ALTO//2-y))
    for y in range(0, ANCHO// 2 + 1, 10):
        color = generarColor()
        pygame.draw.line(ventana, color, (ANCHO-y, ALTO//2), (ANCHO//2, ALTO//2+y))
    for y in range (0, ALTO//2+1, 10):
        color = generarColor()
        pygame.draw.line(ventana, color, (ANCHO//2, ALTO//2-y), (ANCHO-y, ALTO//2))
    for y in range(0, ALTO//2+1, 10):
        xFinal= y+10
        color = generarColor()
        pygame.draw.line(ventana, color, (ANCHO//2, ALTO//2+y), (0+y, ALTO//2))

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
        reloj.tick(40)
    pygame.quit()
# ---------------------------------------------------------------------------------------


#---------------------------------DibujarCirculos----------------------------------------

def dibujarLineasCirculos(ventana):
    for alfa in range(30,390,30):
        angulosRadianes= math.radians(alfa)
        x=150*math.cos(angulosRadianes)
        y=150*math.sin(angulosRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(x+ANCHO//2), int(ALTO//2-y)),150, 1)

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
        dibujarLineasCirculos(ventana)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
# ---------------------------------------------------------------------------------------


#---------------------------------AproximarPi--------------------------------------------
def aproximarPi(numero):
    suma=0
    for d in range (1,numero+1):
        fraccion= 1/(d**2)
        suma+=fraccion

    Pi= (suma*6)**0.5
    return Pi
# ---------------------------------------------------------------------------------------


#---------------------------------NumeroDe4Digitos/37------------------------------------
def calcularNumerosDe4DigitosDivisiblesEntres37():
    cantidadNumeros= 0
    for numeros in range (1000,10000):
        if numeros%37==0:
            cantidadNumeros+=1
    return cantidadNumeros
# ---------------------------------------------------------------------------------------


#---------------------------------OperacionesCiclo---------------------------------------
def calcularOperaciones():
    operacion1= 0
    for numero1 in range (1,10):
        operacion1= operacion1*10+numero1
        resultado1= operacion1*8+numero1
        print(operacion1,"*8",numero1,"=",resultado1)
    print()
    operacion2= 0
    for digito in range (1,10):
        operacion2 = operacion2*10+1
        resultado2= operacion2*operacion2
        print(operacion2,"*",operacion2,"=",resultado2)
# ---------------------------------------------------------------------------------------


def main():
    print("Misión 5. Selecciones qué quiere hacer.")
    print("1. Dibujar cuadrados y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar círculos")
    print("4. Aproximar PI")
    print("5. Contar divisibles entre 19")
    print("6. Imprimir pirámides de números")
    print("0. Salir")
    print()
    print("¿Qué desea hacer?")

    decision= 100
    while decision!=0:
        decision= int(input("Teclea el número de la selección que desea hacer y presiona ENTER: "))
        if decision == 1:
            dibujarCuadradosCirculos()
        if decision == 2:
            dibujarEstrella()
        if decision == 3:
            dibujarCirculos()
        if decision == 4:
            numero= int(input("Introduce un número para aproximar: "))
            aproximarPi(numero)
            pi= aproximarPi(numero)
            print("El número es:",pi)
        if decision == 5:
            calcularNumerosDe4DigitosDivisiblesEntres37()
            numeros= calcularNumerosDe4DigitosDivisiblesEntres37()
            cantidadNumeros= calcularNumerosDe4DigitosDivisiblesEntres37()
            print("La cantidad de números divisibles es de:",cantidadNumeros)
        if decision == 6:
            calcularOperaciones()
        elif decision<0 or decision>6:
            print ("Número invalido")
    print ("EXIT")

main()