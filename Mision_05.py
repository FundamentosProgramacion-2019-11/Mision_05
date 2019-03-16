import pygame
import math


ANCHO = 800
ALTO = ANCHO

BLANCO = (255, 255, 255)  #color
NEGRO= (0, 0, 0)

def main():
    choice=10
    print("Misión 5. Seleccione qué desea hacer.")
    print("1. Dibujar cuadros y círculos.")
    print("2. Dibujar círculos.")
    print("3. Dibujar espiral.")
    print("4. Aproximar Pi")
    print("5. Contar divisibles entre 37")
    print("6. Imprimir pirámides de números.")
    print("0. bye")
    while choice !=0:
        choice=int(input("Cual gusta? "))
        if choice>6 or choice<0:
            print("error, prro")
            choice=10
        elif choice==1:
            dibujarCuadrosCirculos()
        elif choice ==2:
            dibujarCirculos()
        elif choice == 3:
            dibujarEspiral()
        elif choice == 4:
            n = int(input("Teclea el ultimo del último divisor: "))
            calcularSerie(n)

        elif choice == 5:
            divisibles37()
        elif choice == 6:
            numeroscool()
    else:
        print("By(t)e")

# dibujo

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
        pos = ALTO // 2
        for radius in range(1, pos+1, 10):
            pygame.draw.circle(ventana, NEGRO, (pos, pos), radius, 1)
            pygame.draw.rect(ventana, NEGRO, (pos - radius, pos - radius, 2 * radius, 2 * radius), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

#
def dibujarCirculos(): #
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        pos = ALTO // 2
        angulo = (math.pi) / 2
        incremento = (math.pi) / 6
        for centro in range(1,13):
            pygame.draw.circle(ventana, NEGRO,(int(pos - (150 * math.cos(angulo))), int(pos - (150 * math.sin(angulo)))), 150, 1)
            angulo += incremento

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        lineas = (ALTO) // 10 // 2
        for i in range(0, lineas):
            delta = i * 10
            k = ALTO - 2 - delta
            pygame.draw.line(ventana, NEGRO, (k, k), (ALTO - k, k))
            pygame.draw.line(ventana, NEGRO, (k - 10, ALTO - k),
                             (ALTO - k, ALTO - k))
            pygame.draw.line(ventana, NEGRO, (ALTO - k, k), (ALTO - k, ALTO - k))
            pygame.draw.line(ventana, NEGRO, (k - 10, k - 10), (k - 10, ALTO - k))
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


#4.AproxPi
def calcularSerie(n):
    d = 0
    for x in range(1, n + 1):
        d = d + 1 / (x ** 2)

    f = math.sqrt(d * 6)
    print(f)


#5.dvisibles entre 37
def divisibles37 ():
    n=0
    for x in range (1000,10000):
        if x%37==0:
            n = n +1
    print (n)

#6.numeroscool
def numeroscool ():

    f = 0
    x = 1
    n = 0

    for i in range (1,10):
        f = f + x
        x = x * 10
        n = n + f
        print (n, "* 8","+", i, "=", n*8+i)

    d = 0
    sum= 1
    for x in range (1,10):
        d = d + sum
        sum = sum * 10
        print (d, "*", d, "=", d*d)

# REGLA ROTA: NO USAR CADENAS
# ENVIELE ESTO A 10 PROFESORES O TENDRA CUATRO SEMESTRES DE MALA SUERTE ;) 




main()