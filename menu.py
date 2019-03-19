# Autor: Jose Luis Mata Lomeli
# Usando ciclos realizar diferentes figuras mediante funciones y crear un menu 

import pygame   # Librería de pygame.
import random   # Librería random.

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)


def dibujarCuadrosCirculos(ventana):
    for radio in range(1, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio,1)
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2-radio, ALTO//2-radio, radio*2, radio*2), 1)


def dibujarEstrella(ventana):
    for x in range(0, ANCHO // 2, 10):
        al_azar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana, al_azar, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x))  # Lado Izquierdo Superioi
        pygame.draw.line(ventana, al_azar, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x))  # Lado Izquierdo Inferior
        pygame.draw.line(ventana, al_azar, (ANCHO - x, ANCHO // 2),(ANCHO // 2, ANCHO // 2 - x))  # Lado Derecho Superior
        pygame.draw.line(ventana, al_azar, (ANCHO - x, ANCHO // 2),(ANCHO // 2, ALTO // 2 + x))  # Lado Derecho Inferior


def dibujarEspiral(ventana):
    pygame.draw.line(ventana, ROJO, (410, ALTO // 2), (405, ALTO // 2))
    # luego doy la vuelta a la izquierda y sigo
    pygame.draw.line(ventana, ROJO, (410, ALTO // 2 - 10), (410, ALTO // 2))

    for y in range(10, 400, 10):
        # Lineas de Arriba
        pygame.draw.line(ventana, AZUL, (ANCHO // 2 - y, ALTO // 2 - y), (ANCHO // 2 + y, ALTO // 2 - y))
        # Lineas de Izquierda
        pygame.draw.line(ventana, AZUL, (ANCHO // 2 - y, ALTO // 2 - y), (ANCHO // 2 - y, ALTO // 2 + y))
        # Lineas de Abajo
        pygame.draw.line(ventana, AZUL, (ANCHO // 2 - y, 400 + y), (410 + y, ALTO // 2 + y))
        # Lineas de Derecha
        pygame.draw.line(ventana, AZUL, (410 + y, 390 - y), (410 + y, ALTO // 2 + y))


def dibujarCuadro(ventana):
    for y in range(10, 400, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO//2-y, ALTO//2-y), (ANCHO//2+y, ALTO//2-y))
        pygame.draw.line(ventana, NEGRO, (ANCHO//2-y, ALTO//2-y), (ANCHO//2-y, ALTO//2+y))
        pygame.draw.line(ventana, NEGRO, (ANCHO//2-y, 400+y), (410+y, ALTO//2+y))
        pygame.draw.line(ventana, NEGRO, (410+y, 390-y), (410+y, ALTO//2+y))


def dibujarCirculos(ventana):
    for x in range(0, 77, 76):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2-x, 250+(x//4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2+x, 250+(x//4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2-x, 550-(x//4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2+x, 550-(x//4)), 150, 1)

    for y in range(0,141,140):
        pygame.draw.circle(ventana, NEGRO, (250+(y//8), 400-(y//2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (550-(y//8), 400-(y//2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (250+(y//8), 400+(y//2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (550-(y//8), 400+(y//2)), 150, 1)


# Funcion dibujar o Pygame
def dibujar(opcion):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        if opcion == 1:
            dibujarCuadrosCirculos(ventana)

        if opcion == 2:
            dibujarEstrella(ventana)

        if opcion == 3:
            dibujarEspiral(ventana)

        if opcion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

# Funcion que, dado un parametro, determina una aproximacion de Pi
def aproximarPi(n):
    suma = 0 # Acumulador de fracciones
    for divisor in range(1, n+1): #1, 2, 3,..., n
        fraccion = 1/divisor**2
        suma += fraccion #acumular las fracciones hasta llegar al n del rango

    aproxPi = (6*suma)**0.5 #Una vez calculadas las fraccion ormula para aproximar PI
    return aproxPi


# num. divisibles entre 37
def divisor37():
    suma = 0
    for x in range(100, 1000):
        if x//37 == 0:
            print(x)
            suma = suma + 1
    return (suma)


#Funcion para crear piramides de operaciones
def piramides():
    suma1 = 0
    for x in range(1, 10):
        suma1 = suma1*10+1 # 1, 11, 111, 11111,....
        print(suma1, "*", suma1, "=", suma1 * suma1)
        # 1 * 1 = 1
        # 11 * 11 = 121
        # 111 * 111 = 12321
        # ...

    suma2 = 0
    for x in range(1,10):
        suma2 = (suma2*10) + x  #1, 12, 123, 1234,...
        print(suma2, "*", "8", "+", x, "=", suma2*8+x)
        # 1 * 8 + 1 = 9
        # 12 * 8 + 2 = 98
        # 123 * 8 + 3 = 987'
        # ...

################################################################

# Funcion de menu
def leerOpcionMenu():
    print("Menú principal")
    print("1. Dibujar Cuadrados y Circulos")
    print("2. Dibujar Estrella")
    print("3. Dibujar Espiral")
    print("4. Dibujar Circulos")
    print("5. Aproximar a Pi")
    print("6. Contar divisibles de 37")
    print("7. Imprimir piramides de numeros")
    print("0. Salir")

    opcion = int(input('Teclea tu opcion: '))
    return opcion

#Funcion Principal
def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujar(opcion)

        elif opcion == 2:
            dibujar(opcion)

        elif opcion == 3:
            dibujar(opcion)

        elif opcion == 4:
            dibujar(opcion)

        elif opcion == 5:
            terminos = int(input("Teclea la cantidad de terminos deseados: "))
            aproxPi = aproximarPi(terminos)
            print("Pi = ", aproxPi)

        elif opcion == 6:
            d37 = divisor37()
            print('Hay', d37, 'numero(s) divisibles entre 37')

        elif opcion == 7:
            piramides()

        opcion = leerOpcionMenu()
    print("Termina programa")

main()

