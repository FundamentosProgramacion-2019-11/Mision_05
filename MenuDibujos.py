# Autor: Mario Hernández Cárdenas
# Menú dibujos, Tarea 5


from random import randint
import pygame  # Librería de pygame
import math


ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)  # nada de rojo, ni verde, ni azul


def dibujarCuadrosCirculos(ventana):
    for x in range(10, ANCHO // 2 + 1, 10):
        pygame.draw.rect(ventana, NEGRO, (x, x, ANCHO - x * 2, ALTO - x * 2), 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1)


def dibujarEstrella(ventana):
    for avance in range(0, ANCHO // 2 + 1, 10):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.lines(ventana, color, True, [(0 + avance, ALTO // 2), (ANCHO // 2, ALTO // 2 - avance),
                                                 (ANCHO - avance, ALTO // 2), (ANCHO // 2, ALTO // 2 + avance),
                                                 (0 + avance, ALTO // 2)], 1)


def dibujarEspiral(ventana):
    for avance in range(0, ANCHO // 2, 10):
        if avance < ANCHO // 2 - 10:
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 5 + avance, ALTO // 2 + avance),
                             (ANCHO // 2 + 5 + avance, ALTO // 2 - 10 - avance), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 5 + avance, ALTO // 2 - 10 - avance),
                             (ANCHO // 2 - 10 - avance, ALTO // 2 - 10 - avance), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 10 - avance, ALTO // 2 - 10 - avance),
                             (ANCHO // 2 - 10 - avance, ALTO // 2 + 10 + avance), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - avance, ALTO // 2 + avance),
                             (ANCHO // 2 + 5 + avance, ALTO // 2 + avance), 1)
        else:
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - avance, ALTO // 2 + avance),
                             (ANCHO // 2 + 5 + avance, ALTO // 2 + avance), 1)


def dibujarCirculos(ventana):
    for grados in range(0, 331, 30):
        radianes = math.radians(grados)
        x = math.cos(radianes)
        y = math.sin(radianes)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + (int(x * 150)), ALTO // 2 - (int(y * 150))), 150, 1)


def aproximarPi(n):
    suma = 0
    for d in range(1, n + 1):  # 1,2,3...n
        fraccion = 1 / d ** 2
        suma += fraccion

    suma = suma * 6
    aproxPI = suma ** 0.5
    return aproxPI


def divisiblesEntre37():
    totalPDiv = 0
    for pD in range(1000, 10000):
        if pD % 37 == 0:
            totalPDiv += 1
            print("%d es divisible entre 37" % pD)
    print("\nHay un total de %d de números divisibles entre 37" % totalPDiv)


def imprimirPiramidesNumeros():
    piramide1 = 0
    numeroGuardado = 0
    print("\n")
    for potencia in range(0, 9):
        valor = 1 + 10 ** potencia
        piramide1 += valor - 1 ** potencia
        numeroGuardado += piramide1
        primerPiramide = (numeroGuardado * 8 + (potencia + 1))
        print(numeroGuardado, "* 8 +", potencia + 1, "=", primerPiramide)

    piramide2 = 0
    print("\n")
    for potencia in range(0, 9):
        valor = 1 + 10 ** potencia
        piramide2 += valor - 1 ** potencia
        resultadoPiramide = piramide2 ** 2
        print(piramide2, "*", piramide2, "=", resultadoPiramide)


def dibujar(opcion):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)

        if opcion == 1:
            dibujarCuadrosCirculos(ventana)
        elif opcion == 2:
            dibujarEstrella(ventana)
        elif opcion == 3:
            dibujarEspiral(ventana)
        elif opcion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
          "1. Dibujar cuadro y círculos \n"
          "2. Dibujar parábolas \n"
          "3. Dibujar espiral \n"
          "4. Dibujar círculos \n"
          "5. Aproximar PI \n"
          "6. Contar divisibles entre 37 \n"
          "7. Imprimir pirámides de números \n"
          "0. Salir \n")
    opcion = int(input("¿Qué desea hacer? "))
    while opcion != 0:
        if opcion < 0 or opcion > 7:
            print("\nEse no es un número de opción válida")
            input("\nPresione Intro para continuar")
            print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
                  "1. Dibujar cuadro y círculos \n"
                  "2. Dibujar parábolas \n"
                  "3. Dibujar espiral \n"
                  "4. Dibujar círculos \n"
                  "5. Aproximar PI \n"
                  "6. Contar divisibles entre 37 \n"
                  "7. Imprimir pirámides de números \n"
                  "0. Salir \n")
            opcion = int(input("¿Qué desea hacer? "))
        elif 1 <= opcion <= 4:
            dibujar(opcion)
            print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
                  "1. Dibujar cuadro y círculos \n"
                  "2. Dibujar parábolas \n"
                  "3. Dibujar espiral \n"
                  "4. Dibujar círculos \n"
                  "5. Aproximar PI \n"
                  "6. Contar divisibles entre 37 \n"
                  "7. Imprimir pirámides de números \n"
                  "0. Salir \n")
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 5:
            divisores = int(input(("\nTeclea la cantidad de divisores para aproximar PI: ")))
            if divisores <= 0:
                print("Ese no es un número válido")
            else:
                print("\nEl aproximado de PI es:", aproximarPi(divisores))
                input("\nPresione Intro para continuar")
                print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
                      "1. Dibujar cuadro y círculos \n"
                      "2. Dibujar parábolas \n"
                      "3. Dibujar espiral \n"
                      "4. Dibujar círculos \n"
                      "5. Aproximar PI \n"
                      "6. Contar divisibles entre 37 \n"
                      "7. Imprimir pirámides de números \n"
                      "0. Salir \n")
                opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 6:
            divisiblesEntre37()
            input("\nPresione Intro para continuar")
            print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
                  "1. Dibujar cuadro y círculos \n"
                  "2. Dibujar parábolas \n"
                  "3. Dibujar espiral \n"
                  "4. Dibujar círculos \n"
                  "5. Aproximar PI \n"
                  "6. Contar divisibles entre 37 \n"
                  "7. Imprimir pirámides de números \n"
                  "0. Salir \n")
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 7:
            imprimirPiramidesNumeros()
            input("\nPresione Intro para continuar")
            print("\nMisión 5. Seleccione el número de opción qué quiere hacer. \n"
                  "1. Dibujar cuadro y círculos \n"
                  "2. Dibujar parábolas \n"
                  "3. Dibujar espiral \n"
                  "4. Dibujar círculos \n"
                  "5. Aproximar PI \n"
                  "6. Contar divisibles entre 37 \n"
                  "7. Imprimir pirámides de números \n"
                  "0. Salir \n")
            opcion = int(input("¿Qué desea hacer? "))

    print("\n¡Adiós!")


main()
