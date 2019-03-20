#Autor: Ivana Olvera Mérida
#Calcular y regresar una aproximación al valor de Pi

#Se pregunta al usuario cuántos términos quiere generar o el último término que quiere
#Elementos que se requieren para que la función que calcule el valor de pi: acumulador, la función tiene que recibir
#el número de términos, multiplicaciones y realizar operación.

def aproximarPi(n):
    suma = 0
    for d in range(1, n+1): #1,2,3...n En esta función SÍ se quiere tomar en cuenta el valor de n
        fraccion = 1/ d**2 #d es el valor que el usuario está ingresando
        suma += fraccion

    aproxPI = (6*suma) ** 0.5 #Despeje
    return aproxPI

def main():
    print(aproximarPi(1000000)) #Si el número es mayor, es más probable aproximarse al valor de pi

main()
