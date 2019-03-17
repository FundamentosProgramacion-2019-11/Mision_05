#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Este programa calculara el total a pagar de todos los boletos en cada zona
import random
import math
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

def dibujarCirculosYCuadros(ventana):
    for radio in range(10,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),radio,1)
        pygame.draw.rect(ventana,NEGRO,(ANCHO//2-radio,ALTO//2-radio,radio*2,radio*2),1)

def dibujarCirculos(ventana):
    for alfa in range(30,361,30):
        angRAdianes = math.radians(alfa)
        x = 150*math.cos(angRAdianes)
        y = 150*math.sin(angRAdianes)
        pygame.draw.circle(ventana, NEGRO, (int(x+ANCHO//2), int(ALTO//2-y)), 150, 1)

def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    return (rojo, verde, azul)

def dibujarLineasEstrella(ventana):
    for y1 in range(0,ALTO//2,10):
        xFinal1 = y1 + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ANCHO//2,y1), (ANCHO//2 + xFinal1, ALTO//2))
    for y2 in range(0,ALTO//2,10):
        xFinal2 = y2 + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ANCHO//2,y2), (ANCHO//2 - xFinal2, ALTO//2))
    for y3 in range(0,ALTO//2,10):
        xFinal3 = y3 + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ANCHO//2,ALTO-y3), (ANCHO//2 - xFinal3, ALTO//2))
    for y4 in range(0,ALTO//2,10):
        xFinal4 = y4 + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana,colorAleatorio,(ANCHO//2,ALTO-y4), (ANCHO//2 + xFinal4, ALTO//2))

def dibujarLineas(ventana):
    for x in range(1,400,10):
        pygame.draw.line(ventana,NEGRO,(405+x,390-x),(390-x,390-x),1)
        pygame.draw.line(ventana,NEGRO,(390-x,390-x),(390-x,410+x),1)
        pygame.draw.line(ventana,NEGRO,(400-x,400+x),(405+x,400+x),1)
        pygame.draw.line(ventana,NEGRO,(405+x,400+x),(405+x,390-x),1)

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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def dibujarDoceCirculos():
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
        dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def dibujarEspiral():
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
        dibujarLineas(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def dibujarCirculosCuadrados():
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
        dibujarCirculosYCuadros(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def aproximarPi(aprox):
    suma = 0
    for d in range(1, aprox + 1):
        fraccion = 1 / d ** 2
        suma = suma + fraccion  # se puede escribir como: suma += fraccion

    aproxPi = (6 * suma) ** 0.5
    print(aproxPi)

def calcularNumerosDivisibles():
    contador = 0
    for x in range(1000, 10000, 1):
        if x%37 == 0:
            contador = contador + 1
        else:
            contador = contador
    print(contador)

def crearPiramide():
    var = 0
    var1 = 0
    var2 = 0
    for diferencial in range(0,9,1):
        base = 10**diferencial
        var1 = base + var1
        var2 =  var2 + var1
        resultado =  var2 * 8 + (diferencial + 1)
        print(var2, "* 8 +", diferencial+1, "=", resultado)
    print( )
    dif = 0
    for multiplo in range(0,9,1):
        base2 = 10**multiplo
        dif = dif + base2
        piramide = dif * dif
        print(dif, "*", dif, "=", piramide)


def main():
    print("""Elige la opcion que llevara a cabo el programa
    1.- Dibujar circulos y cuadros
    2.- Dibujar Parabolas
    3.- Dibujar espiral
    4.- Dibujar Circulos
    5.- Aproximar PI
    6.- Contar divisble entre 37
    7.- Imprimir piramide de numeros
    0.- Salir""")
    opcion = int(input("Inscriba la opcion que desea realizar"))
    while opcion != 0:
        if opcion == 1:
            dibujarCirculosCuadrados()
        elif opcion == 2:
            dibujarEstrella()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarDoceCirculos()
        elif opcion == 5:
            aprox = int(input("Dame la cantidad con la que te quieres aproximar a PI"))
            aproximarPi(aprox)
        elif opcion == 6:
            calcularNumerosDivisibles()
        elif opcion == 7:
            crearPiramide()
        opcion = int(input("Que otra opcion desea realizar ?"))


main()