


import chunk
from pytube import Search


def Opcion1():
    busqueda=str(input("Ingrese texto de busqueda: "))
    items=int(input("Ingrese cantidad de resultados: "))
    b=Search(busqueda)
    resultados=str(b.results)
    #Con b.results se obtienen los 17 valores y luego procedemos a meterlos a una lista, 
    #ya que estos vienen separados por ","
    list=resultados.split(",")
    #Link0 va a ser el primer resultado del la lista. y luego con link_0 extraemos 
    #los caracteres (ID del video).
    #Ciclo para almacenar leer de la lista la cantidad "n" de resultados, extraer el ID
    # y concatenarlo para crear el link completo.
    lista=[]
    for x in range(0,items):
        link0=list[x]
        link_id=link0[43:53]
        print("Resultado de Video #",x," - https://www.youtube.com/watch?v=",link_id)
        lista.append(link_id)

    #Creamos almacenamiento como input para ingresar valores separados por coma. Asimismo la lista "L" para separar los valores
    almacenamiento=input("Ingrese numero de videos de enlaces a almacenar, separados por coma: ")
    L = [int(x) for x in almacenamiento.split(',')]

    #La variable "linkalmacenado" guardara el resultado de la iteración. Este resultado se almacenara en la lista "lista2"
    lista2=[]
    for y in L:
        print("Enlace de Video #",y," - https://www.youtube.com/watch?v="+lista[y],"fue almacenado!")
        linkaalmacenado="https://www.youtube.com/watch?v="+lista[y]
        lista2.append(linkaalmacenado)
    print("")
    
    print(lista2)
    print("")
    print("")





