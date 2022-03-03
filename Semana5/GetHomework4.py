from tokenize import Token
from urllib import response
import webbrowser
import requests
import json, os
from SubirArchivosGitHub import SubirGitHub


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte II
    response=requests.get(Enlace).text
    archivo=open(FilePath, "w")
    if(response=="El key introducido es invalido o aun no esta disponible"):
        print("No hay contenido disponible para esta semana")
        exit()
    try:
        response_info=json.loads(response)
    except:
        print("El contenido de la semana no se encuentra en un formato json valido")
    else:
        json.dump(response_info,archivo,indent=6)
        print("Se almaceno exitosamente al archivo:", FilePath)
    finally:
        archivo.close()
        

InputSemana = input("Ingrese semanas: ")
#Parte IV

InputFile = input("Ingrese\ path y nombre de archivo: ")
#Verificación del Filepath
if(os.path.isdir(os.path.dirname(InputFile))==False):
    print("El path ingresado:", os.path.dirname(InputFile),"No se encuentra, ingrese un path adecuado.")
else:
    GetHomework(InputSemana,InputFile)

"""
Mensaje = input("Ingrese el mensaje del Commit: ")
TokenGithub = input("Ingrese Token para autenticarse a GitHub: ")
Repo = input("Ingrese el Repo de GitHub: ")

SubirGitHub(MensajeCommit=Mensaje, Token=TokenGithub, Archivo=InputFile, NombreRepo=Repo)
"""

