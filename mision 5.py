#Autor: Victor Cerón Navarrete
#Pregunta al usuario que operación quiere que se haga

#Problema: No se cierra la ventana de pygame


import pygame   # se importa pygame
import math #Trigo

# Se pone cuanto mide la pantalla
ANCHO = 800
ALTO = ANCHO
# Colores
BLANCO = (255, 255, 255)
NEGRO= (0, 0, 0) # colores en RGB

def main(): #Le preguntamos al usuario que quiere que haga pycharm

    elegir=10
    print(" Qué deseas que haga el programa? \n1. Dibujar cuadros y círculos.\n2. Dibujar círculos."
          "\n3. Dibujar espiral.\n4. Calcular Pi\n5. Contar divisibles entre 37\n6. Imprimir pirámides de números."
          "\n0. Salir.")
    while elegir !=0: #Mientras el usuario escriba un numero positivo que no sea 0, se podrá seguir corriendo el programa
        elegir=int(input("¿Qué desea hacer? "))
        if elegir>6 or elegir<0:#Si es mayor a 6 o menor a 0, marca error
            print("Ese número no es válido")
            elegir=10
        elif elegir==1:
            print("Elegiste: dibujar cuadros y círculos. Da click en el tache para ejecutar la siguiente instrucción")
            dibujarCuadrosCirculos()
        elif elegir ==2:
            print("Elegiste: dibujar círculos. Da click en el tache para ejecutar la siguiente instrucción")
            dibujarCirculos()
        elif elegir == 3:
            print("Elegiste: dibujar espiral. Da click en el tache para ejecutar la siguiente instrucción")
            dibujarEspiral()
        elif elegir == 4:
            print("Elegiste: calcular Pi.")
            Pi()
        elif elegir == 5:
            print("Elegiste: contar divisibles entre 37.")
            Ndivisibles()
        elif elegir == 6:
            print("Elegiste: imprimir pirámides de números.")
            imprimirOps()
    else:
        print("FIN")#Si se escribe 0, se sale del programa



#Funciones del dibujo
#Cuadrados y círculos
def dibujarCuadrosCirculos(): #Dibuja cuadrados y rectángulos
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:  # Ciclo se repite mientras sea false
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True      # acaba el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
        pos = ALTO // 2 #se pone al centro de la pantalla
        for radius in range(1, pos+1, 10):
            pygame.draw.circle(ventana, NEGRO, (pos, pos), radius, 1)
            pygame.draw.rect(ventana, NEGRO, (pos - radius, pos - radius, 2 * radius, 2 * radius), 1)
        pygame.display.flip() #Para dibujar los rtazos
        reloj.tick(40)
    pygame.quit()


#Círculos
def dibujarCirculos(): #Dibuja 12 círculos
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False #Puede o no terminar la ejecución

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(BLANCO) #Borra pantalla
        x = ALTO // 2 #coordenada  de centro
        angulo = (math.pi) / 2 #Acomulador
        aumento = (math.pi) / 6
        for centro in range(1,13):
            pygame.draw.circle(ventana, NEGRO,(int(x - (150 * math.cos(angulo))), int(x - (150 * math.sin(angulo)))), 150, 1)
            angulo += aumento #Incrementa en 30 grados cada círculo

        pygame.display.flip()  # cambia los trazos
        reloj.tick(40)  # cuantas veces por segundo se dibuja
    pygame.quit()  # termina el programa


#Se dibuja el espiral
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea ventana
    reloj = pygame.time.Clock() #Limita cuadros por segundo
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(BLANCO)
        lineas = (ALTO) // 10 // 2
        for i in range(0, lineas):
            y = i * 10  # Espacio entre lineas
            a = ALTO - 2 - y  #a es donde comienza el espiral, el 2 es el espacio entre el final de la ventana
            pygame.draw.line(ventana, NEGRO, (a, a), (ALTO - a, a))
            pygame.draw.line(ventana, NEGRO, (a - 10, ALTO - a),
                             (ALTO - a, ALTO - a))
            pygame.draw.line(ventana, NEGRO, (ALTO - a, a), (ALTO - a, ALTO - a))
            pygame.draw.line(ventana, NEGRO, (a - 10, a - 10), (a - 10, ALTO - a))
        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()


#Función 4
#Solo funciona si el número es positivo
def Pi():
    n = int(input("Cuantos elementos quieres usar para tu aproximación? "))
    if n > 0:
        pi = despejarPi(n)
        print("Pi vale aproximadamente:", pi)
    else:
        print("No se puede realizar la aproximación con números negativos")

def despejarPi(n):
    pi = (sumarAproximacion(n) * 6) ** (1 / 2)
    return pi

def sumarAproximacion(n): #Calcula el valor aproximado con la fórmula dada.
    aproximacion = 0 #acumulador
    for x in range(1, n + 1): #desde 1 hasta el número que quiere el usuario
        b = (1 / x ** 2)
        aproximacion += b
    return aproximacion

#Funcion numero 5
def Ndivisibles(): #Corre la función que calcula e imprime el resultado.
    divisibles=encontrarN()
    print("El número de números con 4 dígitos divisibles entre 37 es de:", divisibles)

def encontrarN(): #Utiliza un contador
    divisibles=0
    for n in range(1000,10000): #del 1000 al 9999
        if n%37==0: #Suma cada que sea divisible
            divisibles+=1

    return divisibles

#Funciones 6
def imprimirOps(): #calcula la cadena y la imprime
    uno=0 #acumulador 11, 111, 1111...
    for i in range(1,10):
        uno=uno*10+1
        resultado1=uno*uno
        print("%d * %d = %d"%(uno,uno,resultado1))
    print("\n")
    base=0
    for n in range(1,10):
        base=base*10+n # Acomulador 12, 123, 1234...
        resultado2=base*8+n
        print("%d * 8 + %d = %d"%(base,n,resultado2))



main() #Corre la función principal