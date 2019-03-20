#Rafael Romero Bello A01747730
#Mision 5
#19/03/19
import pygame
import random

ANCHO = 800
ALTO = 800

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

def generarColorAlazar():
    AZUL = random.randint(0, 123, 123)
    VERDE = random.randint(0, 55, 0)
    ROJO = random.randint(255, 0, 0)
    return (AZUL, VERDE, ROJO)


def dibujarCuadrosCirculos(ventana):
    for n in range(0, 400, 10):
        pygame.draw.rect(ventana, NEGRO, (395-n, 395-n, 10+(2*n), 10+(2*n)), 1)
    for n in range(10, 400, 10):
        pygame.draw.circle(ventana, NEGRO, (400, 400), n, 1)


def dibujarEstrellas(ventana):
    for n in range(0, 400, 10):
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana, colorAlazar, ((ALTO // 2), n), ((ALTO // 2) + n, (ALTO // 2)))
        pygame.draw.line(ventana, colorAlazar, ((ALTO // 2), n), ((ALTO // 2) - n, (ALTO // n)))
        pygame.draw.line(ventana, colorAlazar, ((ALTO // 2), ALTO - n), ((ALTO // 2) + n, (ALTO // 2)))
        pygame.draw.line(ventana, colorAlazar, ((ALTO // 2), ALTO - n), ((ALTO // 2) - n, (ALTO // 2)))


def dibujarCirculos(ventana):
    for y in range(0, 360, 30):
        x = y
        a = math.radians(x)
        x = 150 * math.cos(a)
        y = 150 * math.sin(a)
        pygame.draw.circle(ventana, NEGRO, (int(x + (ALTO // 2), int(y + (ALTO // 2))), 150, 1))

def piApoximacion(n):
    suma=0
    for z in range(1,n+1):
        ope=1/z**2
        suma+=ope
    pi=(6*suma)**.5
    return pi
def piramide1():
    suma=0
    for n in range(1,10):
        suma=suma*10+n
        total=(suma*8)+n
        print(suma,"*8+",n,"=",total)

def piramide2():
    suma=0
    for n in range(1,12):
        suma=suma*10+1
        total=(suma*suma)
        print(suma,"*",suma,"=",total)

def divisiblesentre3():
    suma=0
    for  n in range(1000,10000):
        if n%37==0:
            suma+=1
        total=suma
    return total

def main():
    print(piApoximacion(2000))
    print(piramide1())
    print(piramide2())
    print(divisiblesentre3())
    print(dibujarCirculos())
    print(dibujarCuadrosCirculos())
    print(dibujarEstrellas())
main()



