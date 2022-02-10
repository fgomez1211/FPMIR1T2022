import webbrowser

SemanaN =input("Ingrese la semana:")    #Ingresar el número de semana en formato: "Semana+N".


def GetHomework(SemanaN):               #Definición de la función GetHomework con el parámetro "SemanaN".
    return(SemanaN)
    

homework = "https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM="+GetHomework(SemanaN)    #Declaración y concatenación.

webbrowser.open(homework, new=2)        #Ejecución de interfaz webbrowser.