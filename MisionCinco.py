#Autor David Yair Fernández Salas, A01747088
#Este programa te muestra varias acciones que puede hacerse en una ventana de pygame

"""Para poder hacer que aparezcan las ventanas emergentes,es necesario importar la biblioteca de pygame
está,nos permite poder visualizar la figura que queremos hacer en una ventana emergente"""
import pygame


"""Se importo random, que es una biblioteca en donde se puede mostrar la figura con varios colores """
import random


"Se importo la biblioteca math,que nos sirve para poder hacer los calculos necesarios para la figura deseada"
import math

"""Estos datos nos sirven, porque son las medidas de la ventana, y hay que definrlos para poder crear las figuras"""
ANCHO = 800
ALTO = 800


"En esta parte, definimos los colores que vamos a usar en las figuras "
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)
#Dentro de los colores se debe de crear una función especial para los colores aleatorios
def coloresRandom(color):
    color = [(139, 0,0),
               (0, 100, 0),
               (0, 0, 139)]
    return random.shuffle(color)


"Esta funcion se usa para dibujar los circulos con cuadrados, va aumanetando 10 pixeles"
def dibujarCuadrosyCirculos(ventana):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(2, ALTO, 20):
            pygame.draw.rect(ventana, NEGRO, [(ANCHO // 2 - x // 2), (ALTO // 2 - x // 2), x, x], 1)

        for r in range(1, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), r, 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    # Después del ciclo principal
    pygame.quit()  # terminar pygame


"""En esta parte, se uso una funcion llamada dibujar circulo, en ella se realiza las operaciones
necesarias para que pueda dibujar el circulo, 12 veces"""
def dibujarCiculos(ventana):
    alfa= 30
    x= 150 *math.cos(math.radians(alfa))
    y = 150 * math.sin(math.radians(alfa))
    pygame.draw.circle(ventana,NEGRO,(int(x)+ANCHO//2,ALTO//2-int(y)),150,1)

def dibujar():
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

        r=150
        angulo=30
        for circulos in range(1, 13):
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(r * math.cos(math.radians(angulo * circulos)))),(ALTO // 2) + (int(r * math.sin(math.radians(angulo* circulos))))),r, 1)
        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarCiculos(ventana)
        pygame.display.flip()
        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame

# Dibujar, aquí haces todos los trazos que requieras
# Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
# Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
"Esta función dibuja las espirales deseadas, y se le resta 10 pixeles para que se puede ver completa en la ventana"
def dibujarEspiral(ventana):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for coordenada in range(10,ALTO//2,10):
            pygame.draw.line(ventana, NEGRO, ((ANCHO + 5) - coordenada, ALTO - coordenada), (0 + coordenada, ALTO - coordenada),1)
            pygame.draw.line(ventana, NEGRO, (0 + coordenada, ALTO - coordenada), (0 + coordenada, 0 + coordenada), 1)
            pygame.draw.line(ventana, NEGRO, (0 + coordenada, 0 + coordenada), (ANCHO - (coordenada), 0 + coordenada), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - coordenada, 0 + coordenada),(ANCHO -coordenada, ALTO - (coordenada + 10)), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - coordenada, ALTO - (coordenada + 10)),((ANCHO - 7) - coordenada, ALTO - (coordenada + 10)), 1)
        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps




"Esta funcion revibe los parametros como los valores que el usario ponga para obtener pi "
def calcularPI(n):
    suma = 0
    for denominador in range(1, n + 1):
        fracción = 1 / denominador ** 2
        suma += fracción

    suma = suma * 6
    aproxPI = suma ** 0.5
    return aproxPI


"Esta función obtiene numeros que sean divisibles entre cierto numero con un contador"
def calcularNumeros():
    contadornumeros = 0
    for numero in range(100, 1000):
        if numero % 37 == 0:
            contadornumeros += 1
    print("Los números divisibles entre 37 con 4 cifras son",contadornumeros)


"ESta funcion hace la tabal de un cierto número y guarda los valores que el usario ha introducido como paramateros para saber el rango de la tabla"
def calcularTabla():
    contador = 0
    for n in range(9):
        print((contador * 10 + n + 1), "*", 8, "+", n + 1, "=",((contador * 10 + n + 1) * 8 + (n + 1)))
        contador = contador * 10 + n + 1


    print("")
    valorsSumado=0
    for o in range(9):
        print((valorsSumado * 10 + 1), "*", (valorsSumado * 10 + 1), "=", ((valorsSumado * 10 + 1)*(valorsSumado * 10 + 1)))
        valorsSumado = valorsSumado * 10 + 1


"Esta funcion main(), es la principal de todo el programa y pregunta al usuario que opción quiere"
"Y envia cada parametro a las demas fucniones dependiendo de la respuesta del usuario"
def main():
    opcion = -1
    while (opcion != 0):
        opcion = int(input('''
        Misión 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar círculos
        5. Aproximar PI
        6. Contar divisibles entre 37
        7. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?: '''))
        if opcion == 1:
            dibujarCuadrosyCirculos(opcion)
        elif opcion == 2:
            dibujarParabola(opcion)
        elif opcion == 3:
            dibujarEspiral(opcion)
        elif opcion == 4:
            dibujar()
        elif opcion == 5:
            divisor = int(input("Introduzca el rango de números que quiere: "))
            p = calcularPI(divisor)
            print(p)
        elif opcion == 6:
            calcularNumeros()
        elif opcion == 7:
            calcularTabla()
        elif opcion == 0:
            print("Terminado")
            break


main()