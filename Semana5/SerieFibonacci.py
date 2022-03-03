
from itertools import count


"""
numero = int(input("Cuantos numero de la Serie Fibonacci quiere imprimir? "))

digito1 = 0
digito2 = 1
conteo = 0

#Verificar que sean numeros positivos
if numero <=0:
    print("Ingresar un número positivo")

#Una solo digito:
elif numero==1:
    print("Secuencia de", numero, "numeros:")
    print(numero)
"""


#Secuencia para mas de 1 números
"""
else:
    print("Secuencia Fibonacci:")
    while(conteo < numero):
        print(digito1)
        digito3 = digito1 + digito2
        digito1 = digito2
        digito2 = digito3
        conteo +=1
"""

#Metodo Alternativo
"""
Num=int(input("Ingrese la cantidad de digitos: "))
PrimerNumero=0
SegundoNumero=1
print(PrimerNumero, end="")
print(SegundoNumero, end="")
for i in range(3, Num+1):
    SiguienteSecuencia = PrimerNumero+SegundoNumero
    print(SiguienteSecuencia, end=" ")
    PrimerNumero=SegundoNumero
    SegundoNumero=SiguienteSecuencia
"""

#FibonacciRecursivo

Num1=int(input("Ingrese la cantidad de digitos: "))
if(Num1<2):
    print("Porfavor ingrese un numero mayor a 2")
    exit()
PrimerNumero=0
SegundoNumero=1
print(PrimerNumero, end=" ")

def FibonacciRecursivo(PrimerNum,SegundoNum,ConteoSecuencia,Limite):
    if(ConteoSecuencia==Limite):
        return SegundoNum
    else:
        print(SegundoNum, end=" ")
        return FibonacciRecursivo(SegundoNum,PrimerNum+SegundoNum)

FibonacciRecursivo(PrimerNumero,SegundoNumero,1,Num1)





