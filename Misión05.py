#Autor: Mariana Teyssier Cervantes
#Misión 05
import random
import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#Opción 1
def dibujarCuadrosCirculos(ventana):
    for radio in range(10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)
    for x in range (10, ANCHO//2+1, 10):
            pygame.draw.rect(ventana, NEGRO, (x, x, ANCHO - x * 2, ALTO - x * 2), 1)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarOpcion1():
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

        dibujarCuadrosCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Opción 2
def generarColor():
    rojo = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)

    return (rojo, verde, azul)


def dibujarEstrella(ventana):
    for y in range(0, ANCHO//2+1, 10):
        xFinal = y+10
        colorAleatorio = generarColor()
        pygame.draw.lines(ventana, colorAleatorio, True, [(0+xFinal, ALTO//2), (ANCHO//2, ALTO//2-xFinal),
                                                          (ANCHO-xFinal, ALTO//2), (ANCHO//2, ALTO//2+xFinal),
                                                          (0+xFinal, ALTO//2)], 1)

def dibujarOpcion2():
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

        dibujarEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Opción 3
def dibujarDoceCirculos(ventana):
    for alfa in range(30, 361, 30):
        angRadianes = math.radians(alfa)
        x = math.cos(angRadianes)
        y = math.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(150 * x + ANCHO//2), int(ALTO//2 - y * 150)), 150, 1)

def dibujarOpcion3():
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

        dibujarDoceCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Opción 4
def aproximarPI(n):
    suma = 0
    for d in range(1, n+1): #1,2...n
        fraccion = 1 / d**2
        suma += fraccion

    aproxPI= (6*suma)**0.5
    return aproxPI

#Opción 5
def numerosDivisibles():
    posiblesDivisores = 0
    for n in range(1000,10000):
        if n%37==0:
            posiblesDivisores+=1

    print("%d números son divisibles entre 37" % posiblesDivisores)

#Opción 6
def imprimirOperaciones():
    n1 = 0
    for n2 in range(1, 10):
        n1 = n1 * 10 + n2
        operacion1 = n1 * 8 + n2

        print(n1, "*8+", n2, "=", operacion1)

    print()

    n3 = 0
    for n4 in range(1, 10):
        n3 = n3 * 10 + 1
        operacion2 = n3 * n3
        print(n3, "*", n3, "=", operacion2)




# Función principal, aquí resuelves el problema
def main():
    print("\nSeleccione la opción qué quiera hacer. \n"
          "1. Dibujar cuadros y círculos \n"
          "2. Dibujar estrella \n"
          "3. Dibujar doce círculos \n"
          "4. Aproximar PI \n"
          "5. Números divisibles entre 37 \n"
          "6. Imprimir operaciones \n"
          "7. Salir \n")
    opcion = int(input("¿Qué quiere hacer?"))

    while opcion!=0:
        if opcion<=0 or opcion>=8:
            print("Número no válido")
            input("Intro para continuar")
        elif opcion == 1:
            dibujarOpcion1()
            input("Intro para continuar")
        elif opcion == 2:
            dibujarOpcion2()
            input("Intro para continuar")
        elif opcion == 3:
            dibujarOpcion3()
            input("Intro para continuar")
        elif opcion == 4:
            n = int(input("Teclea n para aproximarse a PI: "))
            aproximarPI(n)
            print(aproximarPI(n))
            input("Intro para continuar")
        elif opcion == 5:
            numerosDivisibles()
            input("Intro para continuar")
        elif opcion == 6:
            imprimirOperaciones()
            input("Intro para continuar")

        opcion = int(input("¿Qué quiere hacer?"))

        if opcion == 7:
            quit()


# Llamas a la función principal
main()