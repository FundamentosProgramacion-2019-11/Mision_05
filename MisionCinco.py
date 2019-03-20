#AUTOR: Aline Villegas Berdejo
#Hace un menú y ejecuta diferentes funciones (dibujos y calculos) que se le indiquen de acuerdo a lo elegido por el usuario.


import math
import pygame   # Librería de pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO= (0,0,0)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


#Genera colores al azar
def generarColorAzar():
    rojo= random.randint(0,255)
    verde=random.randint(0, 255)
    azul= random.randint(0, 255)
    colorX=(rojo,verde,azul)
    return colorX


#Dibuja en una ventana, cuadros y círculos
def dibujarCuadrosCirculos(ventana):
    for radio in range(5, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)
    lado=10
    for x in range(ALTO//2-5,0, -10):
            pygame.draw.rect(ventana, NEGRO, (x, x, lado, lado), 1)
            lado=lado+20


#Dibuja una estrella con líneas las cuales hacen efecto de parábolas
def dibujarEstrella(ventana):
    for x in range(ANCHO//2, ANCHO, 10):
        y= ALTO - (x - ANCHO // 2)
        colorAzar=generarColorAzar()
        pygame.draw.line(ventana, colorAzar, (x, ALTO//2), (ANCHO//2, y))

    for x in range(ANCHO//2 , 0, -10):
        y= ALTO + (x - ANCHO//2)
        colorAzar=generarColorAzar()
        pygame.draw.line(ventana, colorAzar, (x, ALTO//2), (ANCHO//2, y))

    for x in range(ANCHO//2 , ANCHO,10):
        y = x - ((ALTO // 2) + 1 )
        colorAzar=generarColorAzar()
        pygame.draw.line(ventana, colorAzar, (x, ALTO//2), (ANCHO//2, y))

    for x in range(ANCHO//2 - 10, 0, -10):
        y= (ALTO// 2) - x - 1
        colorAzar=generarColorAzar()
        pygame.draw.line(ventana, colorAzar, (x, ALTO//2), (ANCHO//2, y))


#Dibuja 12 círculos con radio de 150 y ángulo de 30grados entre sí
def dibujarCirculos(ventana):
    alfa=30
    while alfa <= 360:
        x=150 * math.cos(math.radians(alfa))
        y= 150 * math.sin(math.radians(alfa)) + ALTO//2
        pygame.draw.circle(ventana, NEGRO, (int(x)+ ANCHO//2 , int(y)), 150, 1)
        alfa = alfa + 30


#Estructura básica de un programa que usa pygame para dibujar
def dibujar(numero):
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

#Es parte del menú
        if numero == 1:
            dibujarCuadrosCirculos(ventana)
        elif numero == 2:
            dibujarEstrella(ventana)
        elif numero == 3:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Aproxima PI de acuerdo al divisor que el usuario inserte y regresa el valor de PI
def aproximarPI(n):
    suma=0 #la sumatoria de fracciones
    for d in range(1, n+1): #1,2,3...n
        fraccion=1/d**2
        suma += fraccion
    suma= suma*6
    aproxPI=suma** 0.5
    return aproxPI


#Calcula los divisibles de 37 de acuerdo a un número de 4 dígitos
def contarDivisibles():
    contador= 0
    for divisibles in range(1000, 10000, 1):
        if divisibles % 37 == 0:
            contador += 1
    return contador


#Imprime dos piramides de números
def imprimirPiramides():
    x = 0
    for n in range(1, 10):
        x = x * 10 + n
        resultado = x * 8 + n
        print(x, "* 8 + ", n, " = ", resultado)


    for n in range(1,10):
        onces=(10**n - 1 ) // 9
        resultado= onces ** 2
        print(onces, "*",  onces, "=" ,resultado)


# Función principal, aquí resuelves el problema
def main():
    #Aquí empieza el menú
    print("Misión 5. Seleccione qué quiere hacer. \n1. Dibujar cuadros y círculos \n2. Dibujar parábolas \n3. Dibujar círculos \n4. Aproximar PI \n5. Contar divisibles entre 37 \n6. Imprimir pirámides de números \n0. Salir ")
    numero= int(input("¿Qué desea hacer? "))
    while numero != 0:
        if numero <=3 and numero >= 1:
            dibujar(numero)
        elif numero== 4:
            n=int(input("¿Cuál quiere que sea el último divisor para aproximar PI?: "))
            valorPI= aproximarPI(n)
            print("La aproximación de PI es:", valorPI)
        elif numero == 5:
            divisibles=contarDivisibles()
            print("Hay", divisibles, "divisibles entre 37")
        elif numero == 6:
            imprimirPiramides()
        print("Misión 5. Seleccione qué quiere hacer. \n1. Dibujar cuadros y círculos \n2. Dibujar parábolas \n3. Dibujar círculos \n4. Aproximar PI \n5. Contar divisibles entre 37 \n6. Imprimir pirámides de números \n0. Salir ")
        numero = int(input("¿Qué desea hacer? "))



# Llamas a la función principal
main()