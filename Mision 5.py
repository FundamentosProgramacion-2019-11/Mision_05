# encoding: UTF-8
# Autor: Santiago España Vázquez
# Misión 5
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
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)

def calcularPI(n):
    plus=0
    for c in range(1,n+1,1):
        plus+= (1/(c**2))
    plus= (plus*6)**.5
    return plus

def calcularnum4d():
    plus=0
    for c in range(1000,10000):
        if c%37==0:
            plus+=c
    return plus

def piramidesNumeros():
    newHi1=0
    newHi = 0
    for c in range(0,9):
        hi=(10**c)+newHi
        newHi=hi
        newHi1+=newHi
        print(newHi1,"* 8","+",c+1,"=",(newHi1*8+(c+1)))

    newHo=0
    for c in range(0, 9):
        ho = (10 ** c) + newHo
        newHo = ho
        print(ho, "*", ho, "=", ho ** 2)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadrosCirculos(ventana):
    for c in range(0, 400, 10):
        pygame.draw.rect(ventana,NEGRO,(395-c, 395-c, 10+(2*c), 10+(2*c)), 1)
    for c in range(10, 400, 10):
        pygame.draw.circle(ventana,NEGRO,(400,400),c,1)


def generarColor():
    rojo= random.randint(0,255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    return (rojo, verde, azul)

def dibujarEstrella(ventana):
    for c in range(0,400,10):
        colorAleatorio=generarColor()
        pygame.draw.line(ventana, colorAleatorio, ((ALTO//2), c), ((ALTO//2) + c, (ALTO//2)))
        pygame.draw.line(ventana, colorAleatorio, ((ALTO//2), c), ((ALTO//2) - c, (ALTO//2)))
        pygame.draw.line(ventana, colorAleatorio, ((ALTO//2), ALTO-c), ((ALTO//2) + c, (ALTO//2)))
        pygame.draw.line(ventana, colorAleatorio, ((ALTO//2), ALTO-c), ((ALTO//2) - c, (ALTO//2)))



def dibujarEspiral(ventana):
    for c in range(10,400,10):
        pygame.draw.line(ventana, NEGRO, (410-c, 400+c), (400+c, 400+c), 1)
        pygame.draw.line(ventana, NEGRO, (400-c, 400-c), (400-c, 410+c), 1)
        pygame.draw.line(ventana, NEGRO, (400+c, 400-c), (400-c, 400-c), 1)
        pygame.draw.line(ventana, NEGRO, (400 + c, 400 - c), (400 + c, 400 + c), 1)


def dibujarCirculos(ventana):
    for c in range (0, 360, 30):
        alfa=c
        angRadianes = math.radians(alfa)
        x=150*math.cos(angRadianes)
        y=150*math.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO,(int(x+(ALTO//2)),int(y+(ALTO//2))), 150,1)

def dibujar(n):
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
        if n==1:
            dibujarCuadrosCirculos(ventana)
        elif n==2:
            dibujarEstrella(ventana)
        elif n==3:
            dibujarEspiral(ventana)
        elif n==4:
            dibujarCirculos(ventana)
        else:
            pass


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



def main():
    n=1
    while n!=0:
        n=int(input("""Misión 5. Seleccione que quiere hacer.
                       1.Dibujar cuadros y circulos
                       2.Dibujar estrella
                       3.Dibujar espiral
                       4.Dibujar circulos
                       5.Aproximar PI
                       6.Contar divisibles entre 37
                       7.Imprimir piramides de números
                       0.Salir
                       ¿Que desea hacer?  """))
        if n>0 and n<5:
            dibujar(n)
        elif n==5:
            last=int(input("Por favor introduzca el ultimo divisor para calcular PI: "))
            print(calcularPI(last))
        elif n==6:
            print(calcularnum4d())
        elif n==7:
            print(piramidesNumeros())
    print("Gracias por utilizar esta herramienta")

# Llamas a la función principal
main()