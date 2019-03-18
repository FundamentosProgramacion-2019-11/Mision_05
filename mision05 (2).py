#Martha Margarita Dorantes Cordero
#Dibujar círculos y cuadrados



import pygame
import random   # Para generar el color aleatorio
import math     # Para el cálculo de PI y los centros de los círculos

# Dimensiones de la ventana
ANCHO = 800
ALTO = 800

# Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)


def dibujarCuadrosCirculos(ventana):
    reloj = pygame.time.Clock()
    ventana.fill(BLANCO)
    radio = 1             # Inicia en radio 1 que es el tamaño mínimo aceptado para dibujar el circulo y el rectangulo

    while radio < ANCHO // 2:
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - radio, ALTO // 2 - radio, radio * 2, radio * 2),1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2,ALTO // 2),radio,1)
        radio = radio + 10

    pygame.display.flip()
    reloj.tick(40)

def dibujarEstrella(ventana):
    reloj = pygame.time.Clock()
    ventana.fill(BLANCO)
    separacion = 0

    while separacion < ANCHO // 2:
        color_aleatorio = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # Parábola superior izquierda
        pygame.draw.line(ventana, color_aleatorio, (0+separacion,ALTO // 2),(ANCHO // 2 , ALTO // 2 - separacion))
        # Parábola inferior izquierda
        pygame.draw.line(ventana, color_aleatorio, (0+separacion,ALTO // 2),(ANCHO // 2 , ALTO // 2 + separacion))
        # Parábola superior derecha
        pygame.draw.line(ventana, color_aleatorio, (ANCHO - separacion, ALTO // 2),(ANCHO // 2 , ALTO // 2 - separacion))
        # Parábola inferior derecha
        pygame.draw.line(ventana, color_aleatorio, (ANCHO - separacion, ALTO // 2),(ANCHO // 2 , ALTO // 2 + separacion))
        separacion = separacion + 10

    pygame.display.flip()
    reloj.tick(40)

def dibujarEspiral(ventana):
    reloj = pygame.time.Clock()
    ventana.fill(BLANCO)
    direccion = 0   # Variable auxiliar para controlar el sentido en el que se dibujan las líneas
    separacion = 5  
    # Se necesita conocer la posición del punto final de la linea dibujada anteriormente
    anterior = (ANCHO // 2, ALTO //2)
    while separacion < ANCHO:

        # Se calcula la posición del punto final de la línea
        if direccion == 0:                                      # Dibujar linea a la derecha
            siguiente = (anterior[0] + separacion, anterior[1])
        elif direccion == 1:                                    # Dibujar linea hacia arriba
            siguiente = (anterior[0], anterior[1] - separacion)
        elif direccion == 2:                                    # Dibujar linea a la izquierda
            siguiente = (anterior[0] - separacion, anterior[1])
        else:                                                   # Dibujar linea hacia abajo
            siguiente = (anterior[0], anterior[1] + separacion)
        pygame.draw.line(ventana, NEGRO, anterior,siguiente)
        anterior = siguiente
        separacion = separacion + 5
        direccion = (direccion + 1) % 4

    pygame.display.flip()
    reloj.tick(40)

def dibujarCirculos(ventana):
    reloj = pygame.time.Clock()
    ventana.fill(BLANCO)
    radio = 150
    circulos = 0
    dx = 0  # Cambio de posición del centro en x
    dy = 0  # Cambio de posición del centro en y

    while circulos < 12:
        # Se calcula el nuevo centro del siguiente circulo basándose en el ángulo y la hipotenusa (en este caso, el radio).
        dx = int(-math.sin(math.pi * ( 2 - circulos / 6)) * radio) 
        dy = int(math.cos(math.pi * ( 2 - circulos / 6)) * radio)
        centro_circulo = (ANCHO // 2 + dx, ALTO // 2 + dy)
        pygame.draw.circle(ventana, NEGRO, centro_circulo, radio, 1)
        circulos = circulos + 1

    pygame.display.flip()
    reloj.tick(40)

def aproximarPI(n):
    pi = 0
    for i in range(1,n+1):
        pi = pi + (1 / i ** 2)
    pi = math.sqrt(pi * 6)
    return pi

def contarDivisibles():
    num_divisible = 0   # Dado que 0 es divisible por cualquier número distinto de 0
    total_divisibles = 0
    while num_divisible < 10000:    # Números de máximo 4 dígitos
        num_divisible = num_divisible + 37
        total_divisibles = total_divisibles + 1
    return total_divisibles

'''
    Funcionamiento de las ecuaciones.
    Para la segunda pirámide de operaciones:
        Tenemos los ejemplos:
            1 * 1 = 1
            11 * 11 = 121
            111 * 111 = 12321
            ...
        Podemos definir la operación como
            c * c = res
            Donde c = 1, 11, 111, 1111, ...
            Podemos definir a c como sigue:
                Empezamos con c = 0
                Así entonces:
                c_0 = 0
                c_1 = c_0 + 10^0 = 0 + 1 = 1
                c_2 = c_1 + 10^1 = 1 + 10 = 11
                c_3 = c_2 + 10^2 = 11 + 100 = 111
                ...
                En general
                c_i = c_(i-1) + 10^i

    Ahora, para la primer pirámide de operaciones:
        Tenemos los ejemplos:
            1 * 8 + 1 = 9
            12 * 8 + 2 = 98
            123 * 8 + 3 = 987
            ...
        Definimos la operación como:
            a * 8 + b = res
            Donde a = 1, 12, 123, 1234, ...
            b = 1, 2, 3, 4, ...
        Para obtener a, podemos calcularlo en términos de c (de la segunda pirámide) y a:
            Iniciamos a = 0
            Así entonces:
                a_0 = 0
                a_1 = a_0 + c_1 = 0 + 1 = 1
                a_2 = a_1 + c_2 = 1 + 11 = 12
                a_3 = a_2 + c_3 = 12 + 111 = 123
                a_4 = a_3 + c_4 = 123 + 1111 = 1234
                ...
            En general:
                a_i = a_(i-1) + c_i
'''
def imprimirPiramides():
    a = 0
    c = 0

    # Las listas solo se utilizan para almacenar las cadenas de resultados
    # no para generar los operandos.
    operaciones1 = list()
    operaciones2 = list()
    
    for i in range(9):
        
        # Aqui se calculan los resultados
        c = c + 10 ** i
        res1 = c * c
        a = a + c
        res2 = a * 8 + (i + 1)
        
        # Se guardan los resultados en las listas
        operaciones1.append('{0} * 8 + {1} = {2}'.format(a,i+1,res2))
        operaciones2.append('{0} * {1} = {2}'.format(c,c,res1))
    
    # Se imprimen los resultados
    for operacion in operaciones1:
        print(operacion)

    for operacion in operaciones2:
        print(operacion)

def menu():
    print('1. Dibujar cuadros y circulos')
    print('2. Dibujar parábolas')
    print('3. Dibujar espiral')
    print('4. Dibujar circulos')
    print('5. Aproximar PI')
    print('6. Contar números de 4 dígitos divisibles entre 37')
    print('7. Imprimir pirámides de números')
    print('8. Salir')
    print('¿Qué desea hacer?')

def realizarOperacion(opcion,ventana):
    if opcion == '1':
        dibujarCuadrosCirculos(ventana)
    elif opcion == '2':
        dibujarEstrella(ventana)
    elif opcion == '3':
        dibujarEspiral(ventana)
    elif opcion == '4':
        dibujarCirculos(ventana)
    elif opcion == '5':
        n = int(input('Ingresa el numero de iteraciones \'n\' de la función: '))
        print('Resultado de la aproximación: {0}'.format(aproximarPI(n)))
    elif opcion == '6':
        print('Total de divisibles:', contarDivisibles())
    elif opcion == '7':
        imprimirPiramides()
    elif opcion == '8':
        pygame.quit()
        exit()
    else:
        print('Opción inválida')

def main():
    salir = False
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    ventana.fill(BLANCO)
    while not salir:
        menu()
        opcion = input()
        realizarOperacion(opcion,ventana)
        opcion = input('¿Desea continuar? (s/n): ')
        if opcion == 'n' or opcion == 'N':
            salir = True
    pygame.quit()
    exit()

if __name__ == '__main__':
    main()