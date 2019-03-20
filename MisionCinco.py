#Autor:Marianela Contreras
#Programa que muestra un menú al usuario para que seleccione entre dibujar, hacer calculos o salir del programa.

# Autor: Marianela Contreras
import math
import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO = (0,0,0)
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad

# Estructura básica de un programa que usa pygame para dibujar


#función para el dibujo 1, dibuja los cuadrados y círculos
def dibujarCuadrosCirculos(ventana):
    centro = 10
    tamaño = 20
    while centro <= 400:
        while tamaño <= 800:
            pygame.draw.rect(ventana,NEGRO,(centro,centro,ANCHO-tamaño,ALTO-tamaño),1)
            centro += 10
            tamaño += 20

    for radio in range (10,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2), radio, 1)


# función para el dibujo 2, genera los colores aleatorios.
def generarColorAzar():
    rojo= random.randint(0,255)
    verde = random.randint (0,255)
    azul = random.randint (0,255)
    colorX= (rojo,verde,azul)
    return colorX

#función para la el dibujo 2, dibuja la estrella
def dibujarEstrella(ventana):
    for x in range (400,ANCHO + 1,10):      #valor de x: horizontal
        y= ALTO - (x-400)-10                #valor de y: vertical
        colorAzar= generarColorAzar()
        pygame.draw.line(ventana,colorAzar,(x,400),(400,y))
    for y in range (0,ALTO//2 + 1,10):
        x= ANCHO//2 - y
        colorAzar= generarColorAzar()
        pygame.draw.line(ventana,colorAzar,(400,y),(x,400))
    for y in range (0,ALTO//2 + 1,10):
        x= ANCHO//2 + y
        colorAzar=generarColorAzar()
        pygame.draw.line(ventana,colorAzar,(400,y),(x,400))
    for x in range (0,ANCHO//2+1,10):
         y= ALTO +(x-400)+10
         colorAzar= generarColorAzar()
         pygame.draw.line(ventana,colorAzar,(x,400),(400,y))


#función para el dibujo 3, dibuja la espiral
def dibujarEspiral(ventana):
    y = 400
    x = 400
    diferencia = 10
    línea = 1
    combinación1 = 1
    combinación2 = 1
    combinación3 = 1
    combinación4 = 1
    while línea < 158:
        if línea == 1:
            pygame.draw.line(ventana, NEGRO, (x,y),((x+5),y))
            x = 400 + 5
        elif línea%2 == 0 and y >= 400:
            pygame.draw.line(ventana, NEGRO, (x,y), (x,400-(combinación1*diferencia)))
            y = 400 - (combinación1*diferencia)
            combinación1 += 1
        elif línea%2 != 0 and x > 400:
            pygame.draw.line(ventana, NEGRO, (x,y), (400 - (combinación2*diferencia),y))
            x = 400 - (combinación2*diferencia)
            combinación2 += 1
        elif línea%2 == 0 and y < 400:
            pygame.draw.line(ventana, NEGRO, (x,y), (x,400 + (combinación3*diferencia)))
            y = 400 + (combinación3*diferencia)
            combinación3 += 1
        elif línea%2 != 0 and x < 400:
            pygame.draw.line(ventana, NEGRO, (x,y), (400 + (combinación4*diferencia),y))
            x = 400 + (combinación4*diferencia)
            combinación4 += 1
        línea += 1


#funcion para dibujar la figura 3, dibuja 12 círculos
def dibujarCirculos(ventana):
    alfa = 30
    x= 150 *math.cos(math.radians(alfa))
    y = 150 * math.sin(math.radians(alfa))
    pygame.draw.circle(ventana,NEGRO, (int(x)+ ANCHO//2,int(y)+ALTO//2),150, 1)

    for alfa in range (30, 361, 30):
        x = 150 * math.cos(math.radians(alfa))
        y = 150 * math.sin(math.radians(alfa))
        pygame.draw.circle(ventana, NEGRO, (int(x) + ANCHO // 2, int(y) + ALTO // 2), 150, 1)

#función para aproximar Pi, recibiendo un valor como parámetro
def aproximarPI(numero):
    suma=0
    for denominador in range (1,numero+1):
        fraccion = 1/denominador**2
        suma +=fraccion

    suma = suma*6
    aproxPi= suma**0.5
    return aproxPi

#función que calcula y regresa la cantidad de números de 4 dígitos, que son divisibles entre 37.
def divisible():
    divisibles= 0
    for digitos in range (1000,10000,1):
        if digitos%37 ==0:
            divisibles += 1
        else:
            pass
    return divisibles

#función para la piramide de numeros, que calcula e imprime operaciones usando un ciclo para cada una.
#función del primer ciclo
def ImprimirprimerCiclo():
    multiplicación = 1
    diferencia = 1
    suma = 1
    for x in range (1,10,1):
        resultado = (8*multiplicación)+suma
        print (multiplicación,"* 8 +",x,"=",resultado)
        diferencia = diferencia*10 + 1
        multiplicación = multiplicación + diferencia
        suma += 1


#función del segundo ciclo
def ImprimirSegundoCiclo():
    aumento= 1
    for x in range (1,10,1):
        resultado = aumento**2
        print (aumento,"*",aumento,"=",resultado)
        aumento= aumento*10 + 1


#función que hace que se dibujen todas las funciones
def dibujar(seleccion):
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
        # condicionar para que solo dibuje una función
        if seleccion == 1:
            dibujarCuadrosCirculos(ventana)
        elif seleccion == 2:
            generarColorAzar()
            dibujarEstrella(ventana)
        elif seleccion == 3:
            dibujarEspiral(ventana)
        elif seleccion == 4:
            dibujarCirculos(ventana)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



def main():
    print("Misión 5. Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
    seleccion= int(input("¿Qué deseas hacer? Introduzca el número: "))
    while seleccion !=0:
        if seleccion == 1:
            dibujar(seleccion)
            print ("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion ==2:
            dibujar (seleccion)
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion ==3:
            dibujar (seleccion)
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion==4:
            dibujar(seleccion)
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion==5:
            numero = int(input("Escriba el valor del último divisor:"))
            resultado = aproximarPI(numero)
            print("La aproximación de Pi es:", resultado)
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion ==6:
            números = divisible()
            print(números)
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        elif seleccion ==7:
            resultado= ImprimirprimerCiclo()
            resultado= ImprimirSegundoCiclo()
            print("Seleccione qué quiere hacer.\n 1.Dibujar cuadros y círculos\n 2.Dibujar parábolas\n 3.Dibujar espiral\n 4.Dibujar círculos\n 5.Aproximar PI\n 6.Contar divisibles entre 37 \n 7.Imprimir pirámides de números \n 0.Salir \n")
            seleccion = int(input("¿Qué deseas hacer? Introduzca el número: "))
        else:
            pass


main()
