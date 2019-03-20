#Autor: Ivana Olvera Mérida
#Menú

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(parametro):
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
        if parametro == 1:
            distancia = 0
            n = 0
            i = 0
            while distancia <= ALTO // 2:
                distancia = distancia + 10
                n = n + 1
                i = i + 1
                pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), distancia,1)  # El punto central, únicamenre se aumenta el radio
                pygame.draw.rect(ventana, NEGRO,(distancia, distancia, (ANCHO - distancia * 2), (ALTO - distancia * 2)),1)  # De afuera hacia adentro
        elif parametro == 2:
            distancia = 0
            while distancia <= ALTO // 2:  # Todas las líneas se van a encontrar en el punto central, afuera hacia adentro
                distancia = distancia + 10
                pygame.draw.line(ventana, NEGRO, (0 + distancia, ALTO // 2),
                                 (ANCHO // 2, ALTO // 2 - distancia), 1)
                pygame.draw.line(ventana, NEGRO, (0 + distancia, ALTO // 2),
                                 (ANCHO // 2, ALTO // 2 + distancia), 1)
                pygame.draw.line(ventana, NEGRO, (ANCHO - distancia, ALTO // 2),
                                 (ANCHO // 2, ALTO // 2 - distancia), 1)
                pygame.draw.line(ventana, NEGRO, (ANCHO - distancia, ALTO // 2),
                                 (ANCHO // 2, ALTO // 2 + distancia), 1)

        elif parametro == 3:
            break

        elif parametro == 4:
            radio = 150
            for angulo in range(0, 360 + 1, 30):
                a = math.radians(angulo)  # Conversión de ángulos a radianes
                coordenadaX = int(radio * math.cos(a))  # Función trigonométrica
                coordenadaY = int(radio * math.sin(a))
                pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + coordenadaX), (ALTO // 2 - coordenadaY)), radio, 1)

        elif parametro == 5:
            suma = 0
            n = int(input("Valor n: "))
            for d in range(1, n + 1):  # 1,2,3...n En esta función SÍ se quiere tomar en cuenta el valor de n
                fraccion = 1 / d ** 2  # d es el valor que el usuario está ingresando
                suma += fraccion

            aproxPI = (6 * suma) ** 0.5  # Despeje
            print(aproxPI)

        elif parametro == 6:
            for i in range(1000, 10000):
                n = i % 37
                if n == 0:
                    print(i)

        elif parametro == 7:
            n = 0
            a = 0
            b = 0
            c = 0
            for i in range(1, 10):  # Se va a repetir nueve veces
                n = n + 1
                a = a * 10 + n  # Números del extremo izquierdo
                b = a * 8 + n  # Es la operación completa para obtener el resultado
                print(a,"*8 +",n,"=",b)


            for k in range(1, 10):
                c = c * 10 + 1
                d = c * c
                print(c,"*",c,"=",d)



        elif parametro == 0:
            break

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 37")
    print("7. Imprimir pirámides de números")
    print("0. Salir")

    parametro = int(input("Seleccione qué quiere hacer: "))
    dibujar(parametro)   # Por ahora, solo dibuja



# Llamas a la función principal
main()