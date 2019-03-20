#Autor: Cesar Guzman Guadarrama
#
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
NEGRO = (0, 0, 0)


def dibujarCir(ventana):
    for alfa in range(0, 360, 30):
        x = 150 * math.cos(math.radians(alfa))
        y = 150 * math.sin(math.radians(alfa))
        pygame.draw.circle(ventana, NEGRO, (int(x) + ANCHO //2, int(y) + ALTO//2),150, 1)


def dibujarCirculos(ventana):
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
        # dibujarCuadricula(ventana)
        dibujarCir(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarRectangulos(ventana):
    lado = 10
    for i in range(5, ALTO, 10):
        pygame.draw.rect(ventana, NEGRO, [ANCHO // 2 - i, ALTO //2 - i, lado, lado], 1)
        lado += 20

    for radio in range(10, ALTO//2, 5):
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2, ALTO//2),radio, 1)


def generarColorAzar():
    rojo = random.randint(0, 255)
    azul =random.randint(0, 255)
    verde= random.randint(0,255)
    colorX = (rojo,azul,verde)
    return colorX


def dibujarEstrella(ventana):
    for fila in range(0, ALTO//2, 10):
        coloAzar = generarColorAzar()
        pygame.draw.line(ventana, coloAzar, [ANCHO//2, fila], [ANCHO//2 + fila, ALTO//2],1)

    for fila in range( 0, ALTO // 2, 10 ):
        coloAzar = generarColorAzar()
        pygame.draw.line( ventana, coloAzar, [ANCHO // 2, fila], [ANCHO // 2 - fila, ALTO // 2], 1 )

    for col in range(0, ANCHO//2, +10):
        coloAzar = generarColorAzar()
        pygame.draw.line(ventana, coloAzar, [0 + col, ALTO//2 ], [ANCHO//2 , ALTO//2 + col], 1)

    for x in range(ANCHO//2, ANCHO, +10):
        coloAzar = generarColorAzar()
        y = ALTO - x + 10
        pygame.draw.line(ventana, coloAzar, [ANCHO//2, y + 400], [x, ALTO//2], 1)


def dibujarCuadrosCirculos(ventana):
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
        #dibujarCuadricula(ventana)

        dibujarRectangulos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarParabolas(ventana):
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
        dibujarEstrella(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



#def dibujarCirculos(ventana):
    """for radio in range(150):
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2, ALTO//2), radio, 1)"""


def dibujarEspiral():
    pass


def AproximarPI(n):
    suma = 0
    for n in range(1, n+1):
        fraccion = 1 / n**2
        suma += fraccion
    suma = suma * 6
    PI = math.sqrt(suma)
        #PI = math.sqrt(6((1 / n**2)))
    return (PI)


def ContarDivisibles(n):
    return n % 37 == 0


def ImprimirPiramide():
    x = 0
    y = 0
    z = 0
    for n in range(0,9,1):
        b = 10**n
        y = b + y
        z = z + y
        final = z * 8 + (n + 1)
        print(z, "* 8 +", n+1, "=", final)
    print( )
    d = 0
    for mul in range(0,9,1):
        b2 = 10**mul
        d = d + b2
        p = d * d
        print(d, "*", d, "=", p)

def main():
    print("""Mision 5. Seleccione que quiere hacer 
          1. Dibujar cuadros y circulos
          2. Dibujar parabolas
          3. Dibujar circulos
          4. Aproximar PI
          5. Contar divisibles entre 37
          6. Imprimir piramide de numeros
          0. Salir""")
    tarea = input("Que numero deseas realizar?")
    while tarea != "0":

        if tarea == "1":
            ventana = pygame.display.set_mode( (ANCHO, ALTO) )  # Crea la ventana donde dibujará
            dibujarCuadrosCirculos(ventana)
        elif tarea == "2":
            ventana = pygame.display.set_mode( (ANCHO, ALTO) )  # Crea la ventana donde dibujará
            dibujarParabolas(ventana)
        elif tarea == "3":
            ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
            dibujarCirculos(ventana)
        elif tarea == "4":
            n = int( input( "¿Hasta que número quieres hacer tu aproximación?" ) )
            PIA = AproximarPI(n)
            print(PIA)
        elif tarea == "5":
            Divisibles = 0
            for n in range(1,10000):
                if ContarDivisibles(n):
                    Divisibles += 1
            print("El total de divisibles son: ",Divisibles)

        elif tarea == "6":
            ImprimirPiramide()

        else:
            print("Error")

        tarea = input("Que numero deseas realizar?")

main()