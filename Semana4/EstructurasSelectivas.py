
#IF
"""
Num1=int(input("Ingrese numero1: "))
Num2=int(input("Ingrese numero2: "))



if (Num1==Num2):
    print("Los números", Num1, "y", Num2,"si son iguales")
    #esto todavia es una línea del if

if (Num1>Num2):
    print("El número", Num1, "es mayor que", Num2)
    #Test
"""


#ELIF
"""
Num1=int(input("Ingrese numero1: "))
Num2=int(input("Ingrese numero2: "))
if  Num1==Num2:
    print("Los numeros",Num1, "y",Num2,"si son iguales")
elif Num1>Num2:
    print("El numero", Num1, "es mayor que", Num2)
elif Num2>Num1:
    print("El numero", Num2, "es mayor que", Num1)
"""


#ELSE
"""
ingresos=int(input("cuales son sus ingresos: "))

if(ingresos<10000):
    print("sus ingresos son menores a 10K")
elif(ingresos>=10000 and ingresos<=30000):
    print("sus ingresos se encuentran entre 10K y 30K")
else:
    print("sus ingresos no estan en ninguno de esos rangos")
"""


#IF-ELSE de una linea
"""
#if (Num1==Num2) else print("Los numeros", Num1, "y", Num2, "son diferentes")
print("los numeros", Num1, "y", Num2, "son iguales") if (Num1==Num2) else print("Los numeros", Num1, "y", Num2, "son diferentes")
SonIguales=(True if (Num1==Num2) else False)
print(SonIguales)
"""


#IF anidados
"""
Num1=int(input("ingrse numero1: "))
if(Num1%2==0):
    Num2=int(input("ingrse numero 2: "))
    if(Num2%2==0):
        print("El resultado de", Num1, "elevado a la potencia", Num2,"es:",Num1**Num2)
    else:
        print("El resultado de",Num1,"dividio",Num2,"es:",Num1/Num2)
"""


#pass
"""
Num1=int(input("ingrese numero1:"))
if(Num1%2==0):
    pass
else:
    print("no fue un numero par")
"""

#Switches

Num1=int(input("ingrese numero de dia de la semana:"))
DiasSemana={
    1:"Lunes",
    2:"Martes",
    3:"Miercoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sabado",
    7:"Domingo"
}
print("El dia de la semana para el numero",Num1,"es:",DiasSemana.get(Num1,"No es un dia de la semana"))


#Excepciones
"""
try:
    print("Estoy en el bloque de try")
    print(int(input("Numero1:"))/int(input("Numero2:")))
except ZeroDivisionError:
    print("Acapture un error de división por cero")
except:
    print("Ocurrio otro error")
else:
    print("No hubieron errores")
"""

"""
archivo=open("/Users/fernandogomez/Dropbox/Fernando Gómez/URL/Maestría/1T/Introducción a la Programación/Test.txt","w")
try:
    archivo.write("Test 2")
except:
    print("No se pudo escribir en el archivo")
else:
    print("archivo modificado exitosamente")
finally:
    archivo.close()
    print("Se cerro el archivo exitosamente")
"""