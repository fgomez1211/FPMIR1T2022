

import json, requests, os                                       #Importación de librerias, json, requests y os para FilePath


Semana = input("Ingrese la semana de la forma 'SemanaN': ")     #Usuario ingresa el número se semana en formato "Semana+N"
FilePath = input("Ingrese el directorio del archivo JSON: ")    #Usuario ingresa FilePath + el nombre del archivo con
                                                                #terminación .JSON


response = requests.get("https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM="+Semana).text
response_info = json.loads(response)
out_file = open(os.path.expanduser(FilePath),"w")       
json.dump(response_info, out_file, indent=6)
out_file.close()


'''
Como el FilePath no es de Windows (No me dejo utilizar el doble //), busque una solución para OSX y encontré open(os.path.expanduser())
El FilePath utilizado de prueba es:  /Users/fernandogomez/Dropbox/Fernando Gómez/URL/Maestría/1T/Introducción a la Programación/GitHub/FPMIR1T2022/Tareas/SemanaX.json
Espero sea igual de válido.
'''