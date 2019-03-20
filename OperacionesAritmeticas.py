#Autor: Ivana Olvera Mérida
#Escribe una función que calcula e imprime las siguientes operaciones
#usando un ciclo para cada una. Los datos deben generarse como valores numéricos.

def calcularPiramide():
    n = 0
    a = 0
    b = 0
    c = 0
    for i in range(1,10): #Se va a repetir nueve veces
        n = n + 1
        a = a * 10 + n #Números del extremo izquierdo
        b = a* 8 + n #Es la operación completa para obtener el resultado
        print (a,"*8 +",n,"=",b)

    for k in range(1,10):
        c = c * 10 + 1
        d = c * c
        print(c,"*, c,"=",d)

def main():
    calcularPiramide()
main()
