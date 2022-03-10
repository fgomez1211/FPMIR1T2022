

#Track de Problemas Python

#Menú de Opciones

from datetime import datetime
import webbrowser
import os

menuprincipal = int(input("Menu principal: \n 1- Fecha y hora actual \n 2- Abrir GitHub. \n 3- Guardar un archivo. \n 4- Salir. \n "))

while menuprincipal != 4:

    if menuprincipal == 1:

        actual= datetime.now()
        print("La fecha y hora actual es: ",actual)
        print("")

    elif menuprincipal == 2:
        sitioweb="https://www.github.com"
        webbrowser.open(sitioweb, new=2)

    elif menuprincipal == 3:
        texto=input("Ingrese el texto a almacenar: ")
        file = open("/Users/fernandogomez/Dropbox/Fernando Gómez/URL/Maestría/1T/Introducción a la Programación/Track3.txt","w")
        file.write(texto)
        file.close()
        print ("Se ha generado su archivo correctamente")

    else:

        print ("Por favor ingrese una opción correcta: ")
        print("")

    menuprincipal = int(input("Menu principal: \n 1- Fecha y hora actual \n 2- Abrir GitHub. \n 3- Guardar un archivo. \n 4- Salir. \n "))
    









