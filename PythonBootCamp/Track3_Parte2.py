

#Track de Problemas Python

#Menú de Opciones

from Opcion1 import Opcion1
from Opcion2 import Opcion2
from Opcion3 import Opcion3
from Opcion4 import Opcion4


menuprincipal = int(input("Menu principal: \n 1- Fecha y hora actual \n 2- Abrir GitHub. \n 3- Guardar un archivo. \n 4- Salir. \n "))
while menuprincipal != 4:

    if menuprincipal == 1:
        Opcion1()

    elif menuprincipal == 2:
        Opcion2()

    elif menuprincipal == 3:
        Opcion3()

    else:
        Opcion4()

    menuprincipal = int(input("Menu principal: \n 1- Fecha y hora actual \n 2- Abrir GitHub. \n 3- Guardar un archivo. \n 4- Salir. \n "))
    
