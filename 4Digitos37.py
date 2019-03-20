#Autor: Ivana Olvera Mérida
#Escribe una función que calcula y regresa la cantidad de números de 4 dígitos, que son divisibles entre 37

def calcularDivisibles():
    for i in range (1000, 10000):
        n = i % 37
        if n == 0:
            print(i)

def main():
    calcularDivisibles()

main()
