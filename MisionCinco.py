# encoding: UTF-8
# Autor: José Isidro Sánchez Vázquez
# Mision Cinco
import math
import random
import pygame   # Librería de pygame


print("Seleccione que quiere hacer.")
print("1.-dibujar cuadros y circulos")
print("2.-dibujar parabolas")
print("3.-dibujar circulos")
print("4.-aproximar PI")
print("5.-divisibles entre 37")
print("6.-Imprimir piramides de numeros")
print("0.-Salir")

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)

tecla = int(input("Teclea lo que quieres hacer: "))
# Estructura básica de un programa que usa pygame para dibujar

def dibujarCirculos(ventana):
    for alfa in range(0,360,30):
        x= int(150* math.cos(math.radians(alfa)))
        y= int(150* math.sin(math.radians(alfa)))
        pygame.draw.circle(ventana,NEGRO,((x)+ANCHO//2,ALTO//2-(y)),150,1)


def generarColorAlazar(): #Funcion para generar colores aleatorios
    rojo = random.randint(0,255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo,verde,azul)
    return colorX


def dibujarArcoPos4(ventana):
    for x in range(400,ANCHO+1,10):
        y = ALTO-x+400
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArcoPos3(ventana):
    for x in range(0,400+1,10):
        y = 400+x
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArcoPos2(ventana):
    for x in range(0,400+1,10):
        y = 400-x
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana,colorAlazar,(x,ALTO//2),(ANCHO//2,y))


def dibujarArcoPos1(ventana):
    for x in range(400,ANCHO+1,10):
        y = x-410
        colorAlazar = generarColorAlazar()
        pygame.draw.line(ventana, colorAlazar, (x, ALTO // 2), (ANCHO // 2, y))


def dibujarEstrella(ventana):
    dibujarArcoPos1(ventana)
    dibujarArcoPos2(ventana)
    dibujarArcoPos3(ventana)
    dibujarArcoPos4(ventana)


def dibujarCuadros(ventana):
    for x in range(0,400+1,10):
        y = x
        pygame.draw.rect(ventana, NEGRO,(x,y,(ANCHO-x*2),(ALTO-y*2)),1)


def dibujarcirculo(ventana):
    for radio in range(1,400,10):
        pygame.draw.circle(ventana,NEGRO,(400,400),radio,1)


def dibujarCirulosYCuadros(ventana):
    dibujarCuadros(ventana)
    dibujarcirculo(ventana)


def aproximarPI(n):
    suma = 0
    for d in range(1, n + 1):  # 1,2,3...,n
        fraccion = 1 / d ** 2
        suma += fraccion
    aproPi = (6 * suma) ** 0.5
    return aproPi


def calcularOperaciones():
    acumulador = 0
    segundo = 8
    for a in range(1, 10):
        primero = 10
        acumulador = acumulador * primero + a
        resultado = acumulador * 8 + a
        print(acumulador, "*", segundo, "+", a, "=", resultado)

    print("")
    acumulador = 0
    for b in range(1, 10):
        primero = 10
        acumulador = acumulador * primero + 1
        dos = acumulador
        resultado = acumulador * dos
        print(acumulador, "*", dos, "=", resultado)


def divisiblesEntre37():
    contador = 0
    for x in range(1000,9999+1):
        if x%37==0:
            contador +=1
    return contador


def dibujar(n):
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

        if tecla == 1:
            dibujarCirulosYCuadros(ventana)
        elif tecla==2:
            dibujarEstrella(ventana)
        elif tecla==3:
            dibujarCirculos(ventana)
        elif tecla==4:
            print("el resultado es: ", aproximarPI(n))
            break
        elif tecla ==5:
            print("La cantidad de numeros de 4 digitos divisibles entre 37 son: ",divisiblesEntre37())
            break
        elif tecla==6:
            calcularOperaciones()
            break
        elif tecla==0:
            print("Salir")
            break

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    n=int(input("Teclea el ultimo divisor: "))
    print("  ")
    dibujar(n)   # Por ahora, solo dibuja


# Llamas a la función principal
main()


