
#Conteo de digitos

Num1=int(input("Escriba un numero:"))
ConteoDigitos=0
Numero=Num1
while(Numero!=0):
    ConteoDigitos+=1
    Numero=Numero//10
print("El numero:", Num1, "tiene los siguientes digitos:", ConteoDigitos)



#Conteo de numeros pares
"""
Num1=int(input("Escriba un numero:"))
Listado=list(range(1,Num1+1))
ContadorPares=0
ContadorImpares=0
for i in Listado:
    if(i%2==0):
        ContadorPares+=1
    elif(i%3==0):
        ContadorImpares+=1
print("El contador de numeros pares es: ", ContadorPares)
print("El contador de numeros impares es: ", ContadorImpares)
"""


#Numeros primos ciclos break
"""
Num1=int(input("Escriba un numero1: "))
Num2=int(input("Escriba un numero2: "))
for i in range(Num1, Num2+1):              #Aquí tenemos el rango de numeros a evaluar
    for x in range(2,i):                   #Aquí tenemos el rango de numeros en el denominador,
        if(i%x==0):
            break
    else:
        print("Encontre el numero primo:",i)
"""



#Como funciona esto es que, tenemos 2 numero. Ejemplo: del 5 a 10.
#El va a evaluar los numeros del 5 al 10 (inclusivo) por eso el Num2+1
#El segundo for va a ser el denominador, el que va a determinar cual va a ser primo.
#Un numero primo va a ser divisible solo por 1 y por si mismo.
#El i va de 5 al 10 inclusivo.
#Luego la función if va a dividir el valor de i dentro del valor de x, y x va de 2 hasta i.
#Si encuentra un número cuyo division entregue un resíduo igual a 0, entonces el "break" detiene
#  el ciclo for de "x". Una vez termina el ciclo, "i" toma un nuevo numero y vuelve a iniciar el ciclo "x"
#Cuando el for de "i" termine hasta el valor indicado, se ejecutará el "else".


#Suma de numeros no recursivo
"""
Num1=int(input("Escriba un numero: "))
Sumatoria=0
for i in range(1,Num1+1):
    Sumatoria+=i
print("La suma de los numeros de 1 a",Num1,"es de:",Sumatoria)
"""



#Sumatoria recursiva
"""
Num1=int(input("Escriba un numero: "))
def SumatoriaRecursiva(Num1):
    if(Num1==1):
        return 1
    else:
        return Num1+SumatoriaRecursiva(Num1-1)

print("La suma de los numeros 1 hasta",Num1,"es de:",SumatoriaRecursiva(Num1))
"""

