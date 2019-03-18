#Autor: Elizabeth Citlalli Zapata Cortes
#Progama que contiene los ejercicios de la mision 05.

import math

import random

import pygame


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


#DIBUJAR CUADROS CIRCULOS
def trazarCuadrosCirculos(ventana):
    #CIRCULOS
    for radio in range(10,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2, ALTO//2), radio, 1)
    #CUADROS
        #Utilizar heramienta para dibujar cuadrilatero. Con base en el radio del circulo, el punto inicial del cuadrado es (Alto//2- radio)
        pygame.draw.rect(ventana, NEGRO, (ALTO//2-radio, ALTO//2-radio, 2*radio, 2*radio), 1)


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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        trazarCuadrosCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



#DIBUJAR ESTRELLA
def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)


def dibujarLineasDeLaEstrella(ventana):
    #CuadranteI (x,y)
    for y in range (0, ALTO//2, 10):
        xFinal= y + 410 #El cuadrante mide de 400x400, 1/4 de la pantalla
        colorAleatoreo= generarColor()
        pygame.draw.line(ventana,colorAleatoreo,(ALTO//2,y), (xFinal,ALTO//2))
    #CuadranteII (-x,y)
    for y in range(0, ALTO//2, 10):
            xFinal = 410 - y
            colorAleatorio = generarColor()
            pygame.draw.line(ventana, colorAleatorio, (ALTO//2, y), (xFinal, ALTO//2))
    #CuadranteIII (-x,-y)
    for y in range (0, ALTO//2, 10):
        xFinal= y + 410
        colorAleatoreo= generarColor()
        pygame.draw.line(ventana,colorAleatoreo,(y, ANCHO//2), (ALTO//2,xFinal))
    #Cuadrante IV (x,-y)
    for y in range(0, ALTO // 2, 10):
        xFinal = ALTO - y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ALTO//2, y + ANCHO//2), (xFinal, ALTO//2))


def dibujarEstrella():

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
        dibujarLineasDeLaEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(24)  #fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



#DIBUJAR ESPIRAL



#DIBUJAR CIRCULOS
def dibujarDoceCirculos(ventana):
    #Dibujar circulos 12 veces
    for alfa in range (30, 370,30): #30,60,90,120,150,180,210,240,270,300,340,370
        anguloRad= math.radians(alfa)
        x = 150*math.cos(anguloRad)
        y = 150*math.sin(anguloRad)
        pygame.draw.circle(ventana, NEGRO, (int(x+ALTO//2), int(ALTO//2-y)), 150, 1)


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
        dibujarDoceCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



#CALCULAR UNA APROXIMACIÓN AL VALOR PI
def calcularPI(uDivisor): #parámetro ultimo divisor
    suma = 0
    for d in range(1, uDivisor):
        fraccion = 1 / d ** 2
        suma += fraccion
    aproxPI = (6 * suma) ** 0.5
    print("Aproximado de PI = ", aproxPI)


#CALCULA Y REGRESA LA CANTIDAD DE NUMEROS DE 4 DIGITOS DIVISIBLES ENTRE 37
def esDivisibleEntre37():
    numeros= 0  #Contador de números de 4 digitos
    for n in range(1000,10000):
        if n % 37==0:
            numeros+= 1
    cantidadNumeros = numeros
    print("Cantidad de números de 4 digitos divisibles entre 37 = ", cantidadNumeros)



#CALCULAR E IMPRIMIER LA TABLA DE VALORES NUMERICOS
def calcularPiramideOperaciones():
    #1 * 8 + 1 = 9
    #12 * 8 + 2=
    #numA,numB * 8 + numB = CANTIDAD

    numA = 0
    for numB in range(1,10):
        numA = numA*10 +numB
        cantidad = numA*8+numB

        print(numA,"* 8 +",numB, "=",cantidad)

    print()
    #1 * 1 = 1
    #11 * 11 = 121
    #num1 * num1 = FUNCION
    #(N*10+1) * (N*10+1) = funcion

    num1 = 0
    for n in range (1,10):
        num1 = num1 * 10 + 1
        funcion = num1 * num1

        print(num1, "*", num1, "=", funcion)



def main():
    print("Misión 5. Seleccione que quiere hacer")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 37")
    print("7. Imprimir pirámides de números")
    print("0. Salir")

    numOpcion = int(input("¿Qué desea hacer?"))

    while numOpcion !=0 :
        if numOpcion ==1 :
            dibujarCuadrosCirculos()
        elif numOpcion == 2:
            dibujarEstrella()
        elif numOpcion ==3:
            print("OPCIÓN NO DISPONIBLE POR EL MOMENTO")#dibujarEspiral()
        elif numOpcion == 4:
            dibujarCirculos()
        elif numOpcion == 5:
            udivisor = int(input("Valor del último divisor: "))
            calcularPI(udivisor) #input parámetro ultimo divisor "uDivisor"
        elif numOpcion == 6:
            esDivisibleEntre37()
        elif numOpcion == 7:
            calcularPiramideOperaciones()
        numOpcion = int(input("¿Qué desea hacer?"))





# Llamas a la función principal
main()
