


from distutils.log import error
import os

def Opcion3():
        texto=input("Ingrese el texto a almacenar: ")
        FilePath=input("Ingrese filepath: ")
 
        try:
                file = open(FilePath,"w")
                file.write(texto)

        except FileNotFoundError:
                mensaje= "El filepath ingresado",FilePath," es invalido:"
                print(mensaje)

        else:
                file.close()
                print ("El archivo se ha cerrado exitosamente.")
                print("")
