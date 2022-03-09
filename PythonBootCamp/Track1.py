
#Track de Condiciones Python


#Ejercicio No.1
Entrada=input("Ingrese un caracter alfanumerico: ")

vocales=["a","e","i","o","u"]
if Entrada in vocales:
    print("El caracter",Entrada," es una vocal")
else:
    print("El caracter",Entrada," es una consonante")



#Ejercicio No.2
Lado1=input("Ingrese longitud 1 del triangulo: ")
Lado2=input("Ingrese longitud 2 del triangulo: ")
Lado3=input("Ingrese longitud 3 del triangulo: ")

if Lado1==Lado3!=Lado2:
    print("Es un triangulo Isosceles")
elif Lado1!=Lado2!=Lado3:
    print("El triangulo es Escaleno")
elif Lado1==Lado2==Lado3:
    print("El triangulo es Equilatero")



#Ejercicio No.3
NotaAlumno=int(input("Ingrese la nota del alumno: "))
print("El estudiante aprobó con una nota de ", NotaAlumno) if (NotaAlumno>=65) else print("El estudiante reprobó con una nota de ",NotaAlumno)



#Ejercicio No.4
Num1=int(input("Ingrese numero del mes: "))
Meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}
print("El més",Num1," es ",Meses.get(Num1,"un més invalido"))



#Ejercicio No.5
AñoIngresado=int(input("Ingrese un año: "))
if AñoIngresado%100 and AñoIngresado%400 ==0:
    print("El año ",AñoIngresado," es un año bisiesto")
elif AñoIngresado%100!=0 and AñoIngresado%4==0:
     print("El año ",AñoIngresado," es un año bisiesto")
else:
    print("El año ", AñoIngresado," no es bisiesto")

