#Autor: Ivana Olvera Mérida
#Cuadros y círculos

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
ROSA = (255, 0, 105)
MORADO = (166, 0, 255)
NARANJA = (255, 97, 0)
AMARILLO = (255, 209, 0)
NEGRO = (0,0,0)

def defdibujarCuadrosCirculos(ventana):
    distancia = 0
    n = 0
    i = 0
    while distancia<= ALTO//2:
        distancia = distancia + 10
        n = n+1
        i = i+1
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), distancia, 1) #El punto central, únicamenre se aumenta el radio
        pygame.draw.rect(ventana, NEGRO, (distancia, distancia,(ANCHO - distancia*2),(ALTO - distancia*2)),1) #De afuera hacia adentro

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

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        defdibujarCuadrosCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()

main()