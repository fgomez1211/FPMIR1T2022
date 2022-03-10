


from distutils.log import error
import os

def Opcion3():
        texto=input("Ingrese el texto a almacenar: ")
        FilePath=input("Ingrese filepath: ")
 
        try:
                file = open(FilePath,"w")
                file.write(texto)

        except:
                print("Ocurrió un error al crear el archivo.")
        else:
                file.close()

        finally:
                print ("El archivo se ha cerrado exitosamente.")
                print("")

