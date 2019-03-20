#Autor: Ivana Olvera Mérida
#Dibujar estrella

import random

import pygame  # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
ROSA = (255, 0, 105)
MORADO = (166, 0, 255)
NARANJA = (255, 97, 0)
AMARILLO = (255, 209, 0)


def generarColor():
    rojo = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)

    return (rojo, verde, azul)


def dibujarLineasEstrella(ventana):
    distancia = 0
    while distancia <= ALTO//2: #Todas las líneas se van a encontrar en el punto central, afuera hacia adentro
        distancia = distancia + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (0 + distancia, ALTO//2),(ANCHO//2, ALTO//2-distancia), 1)
        pygame.draw.line(ventana, colorAleatorio, (0 + distancia, ALTO //2), (ANCHO // 2, ALTO // 2 + distancia), 1)
        pygame.draw.line(ventana, colorAleatorio, (ANCHO - distancia, ALTO // 2), (ANCHO // 2, ALTO // 2 - distancia), 1)
        pygame.draw.line(ventana, colorAleatorio, (ANCHO - distancia, ALTO // 2), (ANCHO // 2, ALTO // 2 + distancia), 1)


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
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw


        dibujarLineasEstrella(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujarEstrella()

# Llamas a la función principal
main()