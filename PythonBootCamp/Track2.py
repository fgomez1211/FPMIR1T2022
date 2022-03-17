
#Track de Ciclos Python



#Práctica No.1
"""
Num1=int(input("Ingrese un numero: "))
for x in range (Num1+1,0,-1):
    Num2=x-1
    for i in range(Num2,-1, -1):
        if i==0: 
            break
        else:
            print(i, end=" ")
    print("")
"""



#Práctica No.2
"""
Num1 = (input("Ingrese un número: "))
x = 0
try:
    i = int(Num1)
    while i > 0:
        y = i % 10
        x = (x * 10) + y
        i //= 10
    print('El inverso del número ingresado es: ', x)
except:
    pass
"""



#Ejercicio 3 - Serie
"""
n=int(input("Ingrese Numero: "))
cambio = n
s = 0
print(n,end=" ")
for i in range(1,n):
   s += cambio
   cambio = cambio * 10 + n
   print("+", cambio, end=" ")
print("=",s+cambio, end=" ")
print("")
"""



#Ejercicio 4 - Patrón de Asteriscos
"""
n = 5
#Parte creciente del patrón
for i in range (1, n+1):
    for j in range (i):
        print ("* ", end="")
    print ()
#Parte decreciente del patrón
for i in range (n-1,0, -1):
    for j in range (i):
        print ("* ", end="")
    print ()
"""



#Ejercicio 5 - Impresión de posiciones pares/impares de una lista
"""
lista=[10, 20, 30, 40,  50, 60, 70, 80, 90, 100]
i=0

for i in range (1, len(lista),2):
    print (lista[i], end=" ")

print ("")

for i in range (0, len(lista),2):
    print (lista[i], end=" ")
"""



#Ejercicio 6 - Inversión de Cadena
"""
def inversion_cadena(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

cadena_i = str(input("Ingrese cadena a invertir: "))
print(inversion_cadena(cadena_i))
"""



#Ejercicio 7 - Recursividad
"""
Cadena = input("Ingrese texto a invertir: ")
def recursion(str):
    if len(str) == 0:
        return str
    else:
        return recursion(str[1:]) + str[0]

print("Texto Original: ", Cadena)
print("Texto Intvertido: ", recursion(Cadena))
"""


