#Autor: Eric Andrés Jardón Chao
#La función principal despliega un menú con 6 funciones a ejecutar. Para salir, el usuario teclea 0.
import pygame   # Librería de pygame
import math #Para funciones trigonométricas en dibujarCirculos()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = ANCHO
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO= (0, 0, 0)

def main(): #Despliega el menú. Opciones menores a 0 o mayores a 6 no son válidas.
    choice=10
    print("Misión 5. Seleccione qué desea hacer. \n1. Dibujar cuadros y círculos.\n2. Dibujar círculos."
          "\n3. Dibujar espiral.\n4. Aproximar Pi\n5. Contar divisibles entre 37\n6. Imprimir pirámides de números."
          "\n0. Salir.")
    while choice !=0: #Mientras la elección del usuario no sea "Salir" el programa pregunta qué desea hacer.
        choice=int(input("¿Qué desea hacer? "))
        if choice>6 or choice<0:
            print("Intente con un número válido.")
            choice=10
        elif choice==1:
            print("Seleccionó: dibujar cuadros y círculos.")
            dibujarCuadrosCirculos()
        elif choice ==2:
            print("Seleccionó: dibujar círculos.")
            dibujarCirculos()
        elif choice == 3:
            print("Seleccionó: dibujar espiral.")
            dibujarEspiral()
        elif choice == 4:
            print("Seleccionó: aproximar Pi.")
            aproximarPi()
        elif choice == 5:
            print("Seleccionó: contar divisibles entre 37.")
            encontrardivisibles()
        elif choice == 6:
            print("Seleccionó: imprimir pirámides de números.")
            imprimirOperaciones()
    else:
        print("¡Adiós!")

#FUNCIONES PARA DIBUJO
#CuadrosCírculos
def dibujarCuadrosCirculos(): #Dibuja cuadrados y rectángulos de misma dimensión iterativamente hasta lenar la pantalla, con distancia 10 pixeles entre sí..
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
        pos = ALTO // 2 #Es la coordenada de referencia, se posiciona a la mitad del eje x o y de la pantalla. En este caso es 400.
        for radius in range(1, pos+1, 10): #El contador es el radio para que incremente de 10 en 10 hasta llegar a los extremos.
            pygame.draw.circle(ventana, NEGRO, (pos, pos), radius, 1) #Dibuja un círculo en el centro para cada radio.
            pygame.draw.rect(ventana, NEGRO, (pos - radius, pos - radius, 2 * radius, 2 * radius), 1) #dibuja un rectángulo de dimensiones radio*2 y radio*2

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Círculos
def dibujarCirculos(): #Dibuja 12 círculos alrededor del centro de la pantalla.
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
        pos = ALTO // 2 #coordenada de referencia para el centro de la pantalla.
        angulo = (math.pi) / 2 #Funciona como acumulador, se inicializa en 90 grados.
        incremento = (math.pi) / 6 #Es el incremento de grados: 30
        for centro in range(1,13):  # El centro de cada círculo debe estar a la misma distancia del centro de la pantalla y ocupan los lugares de las horas de un reloj. 360 grados entre 12 es 30
            pygame.draw.circle(ventana, NEGRO,(int(pos - (150 * math.cos(angulo))), int(pos - (150 * math.sin(angulo)))), 150, 1) #Usa seno y coseno para encontrar las distancias en x y y desde el centro.
            angulo += incremento #Incrementa en 30 grados cada vez que traza un círculo.

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Espiral
def dibujarEspiral(): #Dibuja un espiral con líneas rectas.
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
        lineas = (ALTO) // 10 // 2  # dividir el espacio disponible de la pantalla entre 10 pixeles entre líneas y a la mitad.
        for i in range(0, lineas):
            delta = i * 10  # El espacio entre líneas
            k = ALTO - 2 - delta  # 2 pixeles es el margen desde la ventana a la primer línea. K es usado como coordenada referencia, y es el punto  donde comienza el espiral.
            # Horizontales dibujadas una por una de abajo hacia arriba.
            pygame.draw.line(ventana, NEGRO, (k, k), (ALTO - k, k))  # Se trazan de derecha a izquierda.
            # Horizontales dibujadas una por una de arriba hacia abajo.
            pygame.draw.line(ventana, NEGRO, (k - 10, ALTO - k),
                             (ALTO - k, ALTO - k))  # Se trazan de derecha a izquierda
            # Verticales dibujadas una por una de izquierda a derecha
            pygame.draw.line(ventana, NEGRO, (ALTO - k, k), (ALTO - k, ALTO - k))  # Se trazan de abajo hacia arriba
            # verticales dibujadas una por una de derecha a izquierda
            pygame.draw.line(ventana, NEGRO, (k - 10, k - 10), (k - 10, ALTO - k))  # Se trazan de abajo hacia arriba
        #Se forma un espiral desde afuera hacia dentro, trazando líneas desde la derecha hasta el centro y desde la izquierda hasta el centro;
        #el mismo caso para las horizontales.
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#FUNCIONES PARA 4
def aproximarPi(): #Si el número ingresado de elementos es positivo, devuelve una aproximación. Si no, devuelve error.
    n = int(input("Teclea el número de elementos que quieres usar para la aproximación: "))
    if n > 0:
        pi = despejarPi(n)
        print("Valor de pi aproximado:", pi)
    else:
        print("Error: no se puede realizar aproximación")

def despejarPi(n): #Esta función despeja el valor de pi de la suma obtenida por sumarAprox.
    pi = (sumarAprox(n) * 6) ** (1 / 2)
    return pi

def sumarAprox(n): #Calcula el valor aproximado de (pi*pi/6) según la fórmula dada.
    aproximacion = 0 #acumulador
    for x in range(1, n + 1): #desde 1 hasta el número de elementos que ingresó el usuario.
        elemento = (1 / x ** 2)
        aproximacion += elemento
    return aproximacion

#FUNCIONES PARA 5
def encontrardivisibles(): #Corre la función que calcula e imprime el resultado.
    divisibles=encontrarNumeros()
    print("La cantidad de números con 4 dígitos divisibles entre 37 es", divisibles)

def encontrarNumeros(): #Utiliza un contador
    divisibles=0
    for n in range(1000,10000): #los números con 4 dígitos van del 1000 al 9999.
        if n%37==0: #Cada que sea divisble entre 37 suma uno al contador.
            divisibles+=1

    return divisibles

#FUNCIONES PARA 6
def imprimirOperaciones(): #calcula e imprime con formato de cadena cada operación.
    primer=0 #acumulador usado para obtener 11, 111, 1111...
    for i in range(1,10):
        primer=primer*10+1
        resultado1=primer*primer
        print("%d * %d = %d"%(primer,primer,resultado1))
    print("\n")
    base=0
    for digito in range(1,10):
        base=base*10+digito #Acumulador usado para obtener 12, 123, 1234...
        resultado2=base*8+digito
        print("%d * 8 + %d = %d"%(base,digito,resultado2))



main() #Corre la función principal (el menú).