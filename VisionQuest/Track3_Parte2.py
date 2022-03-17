

#Track de Problemas Python

#Menú de Opciones

from Opcion1 import Opcion1
from Opcion7 import Opcion7


menuprincipal = int(input("Menu principal: \n 1- Búsqueda de Video \n 2- Descargar Video. \n 3- Comprimir y Descomprimir Videos. \n 4- Selección de frames en video. \n 5- Identificar contenido en video. \n 6- Reporte de contenido. \n 7. Salida. \n "))

while menuprincipal != 4:

    if menuprincipal == 1:
        print("")
        Opcion1()

    elif menuprincipal == 2:
        Opcion2()

    elif menuprincipal == 3:
        Opcion3()
    
    elif menuprincipal == 4:
        Opcion4()

    elif menuprincipal == 5:
        Opcion5()

    elif menuprincipal == 6:
        Opcion6()

    elif menuprincipal == 7:
        Opcion7()

    else:
        Opcion7()

    menuprincipal = int(input("Menu principal: \n 1- Búsqueda de Video \n 2- Descargar Video. \n 3- Comprimir y Descomprimir Videos. \n 4- Selección de frames en video. \n 5- Identificar contenido en video. \n 6- Reporte de contenido. \n 7. Salida. \n "))

    
