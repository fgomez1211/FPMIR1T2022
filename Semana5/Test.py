import webbrowser
import requests
import json
from SubirArchivosGitHub import *
import os


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(x,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api","Semana"+str(x))
    webbrowser.open(Enalce, new=2)
    #Parte II
    response=requests.get(Enalce).text

    if(response.capitalize()=="El key introducido es invalido o aun no esta disponible"):
        print("La semana elegida:",str(x),"aun no se encuentra, intente otra semana")
        print("se almacenaron los archivos exitosamente hasta la semana:" + str(x-1))
        exit()
    try:
        response_info=json.loads(response)
        archivo=open(str(FilePath+"Semana"+str(x) +".json"), "w")
        json.dump(response_info,archivo,indent=6)
    except:
        print("No se logro modificar el archivo")
    else:        

        print("Se almaceno exitosamente el archivo para la semana:" + str(x))

    finally:
        if ( x == InputSemana):
            print("se lograron descargar todas las semanas exitosamente")
    archivo.close()


#GetHomework(Num)

InputSemana = int(input("Ingrese semanas a verificar:"))
InputFile = input("Ingrese path:")
x = int(1)
while(x <= InputSemana):

    if(not(os.path.isdir(os.path.dirname(InputFile)))):
        print("El path ingresado:",os.path.dirname(InputFile),"no se encuentra, porfavor ingrese un path valido")
        break
    else:
        GetHomework(x,InputFile)  
        x =x+1