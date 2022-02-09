
from hashlib import new
import webbrowser

Num =input("Ingrese la semana")          #Ingresar el número de semana y se almacena en la variable Num


def GetHomework(SemanaN):               #Definición de la función GetHomework con el parámetro "SemanaN"
    return(f"Semana{SemanaN}")
    
GetHomework(Num)                        #Ejecución de la función GetHomwork con "Num"

Semana = str(GetHomework(Num))          
link = "https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM="

homework = link+Semana                  #Concatenación en variable "homework"

webbrowser.open(homework, new=2)        #Ejecución de interfaz webbrowser.2