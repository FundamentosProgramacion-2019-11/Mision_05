#María Angélica Hernández Parada
#Programa con ciclos y muchas funciones

import pygame   # Librería de pygame
import math
import random
#1) PRIMERAS FUNCIONES PARA DIBUJAR

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)

#Opcion a)
def dibujarCuadrosyCirculos(ventana):
    pygame.init()
    #Para dibujar los circulos
    for radio in range(10,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO, (ANCHO // 2, ALTO // 2),radio,1)

    #Para dibujar los cuadrados
    for x in range(10,ANCHO//2+1,10):
        pygame.draw.rect(ventana,NEGRO, (x,x, ANCHO-x*2, ALTO-x*2),1)


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

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        dibujarCuadrosyCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Opcion b)
def generarColor():
    rojo = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    return (rojo, verde, azul)


def dibujarLasLineasEstrella(ventana):

    #Esta solo hace el lado derecho, superior
    for y in range (0,ALTO//2,10):
        xFinal = y + 410
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ALTO//2,y),(xFinal,ALTO//2))
    # Esta hace el lado izquierdo, superior
    for y in range(0, ALTO // 2, 10):
        xFinal = 410 - y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ALTO // 2, y), (xFinal, ALTO // 2))
    # Esta hace el lado izquierdo, inferior
    for y in range(0, ALTO // 2, 10):
        xFinal = y + 410
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (y, ANCHO//2), ( ALTO // 2,xFinal))
        # Esta hace el lado derecho, inferior
    for y in range(0, ALTO // 2, 10):
        xFinal = ALTO - y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ALTO//2, y + ANCHO//2), (xFinal,ALTO // 2))


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

        dibujarLasLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Opcion d)
def dibujarDoceCirculos(ventana):

    for alfa in range(30,390,30):
        anguRadianes = math.radians(alfa)
        x = 150 *math.cos(anguRadianes)
        y = 150 *math.sin(anguRadianes)
        pygame.draw.circle(ventana,NEGRO,(int(x+ANCHO//2),int(y+ALTO//2)),150,1)


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
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#2) FUNCION QUE CALCULA Y REGRES UANAPROXIMACION DE PI
def calculaPI(n): #parámetro ultimo divisor
    suma=0
    for d in range(1, n):
        fraccion = 1 / d ** 2
        suma += fraccion
    calcuPI= (6 * suma) ** 0.5
    return calcuPI

#3) FUNCION QUE CALCULA Y REGRESA LA CANTIDAD DE NUMEROS DE 4 DIGITOS, QUE SON DIVISIBLES ENTRE 37
def esDivisible37():
    numeros=0
    for n in range(1000, 10000):
        if n%37== 0:
            numeros+= 1
    return numeros

#4) FUNCION QUE CALCULA E IMPRIME OPERACIONES HACIENDO UNA PIRAMIDE
def piramideNumeros():
    numeroA = 0
    for numeroB in range(1,10):
        numeroA = numeroA*10 +numeroB
        valor = numeroA*8+numeroB

        print(numeroA,"* 8 +",numeroB, "=",valor)

    print()

    numero1 = 0
    for n in range (1,10):
        numero1 = numero1 * 10 + 1
        valor = numero1 * numero1

        print(numero1, "*", numero1, "=", valor)


#Funcion principal donde llamo a todas las funciones
def main():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar estrella")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 37")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    pregunta = int(input("¿Qué desea hacer?"))

    while pregunta != 0:
        if pregunta == 1:
            dibujarCuadrosCirculos()
        elif pregunta == 2:
            dibujarEstrella()
        elif pregunta == 3:
            print("EJERCICO NO CONCLUIDO ")  # dibujarEspiral()
        elif pregunta == 4:
            dibujarCirculos()
        elif pregunta == 5:
            n = int(input("Ingresa el último divisor: "))
            print(calculaPI(n))
        elif pregunta == 6:
            print(esDivisible37())
        elif pregunta == 7:
            piramideNumeros()
        pregunta = int(input("¿Qué desea hacer?"))


main()