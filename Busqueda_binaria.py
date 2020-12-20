import random

def busqueda_binaria(lista, comienzo, final, objetivo,iteraciones=0):
    iteraciones += 1
    print (f' buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
   
    if comienzo > final:
        return (False,iteraciones)
    medio = (comienzo + final)// 2

    if lista[medio]== objetivo:
        return (True,iteraciones)
    elif lista [medio]< objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iteraciones)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iteraciones)


if __name__ == "__main__":
    tamano_de_lista= int(input('de que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar?'))

    lista= sorted([random.randint(0,100) for i in range (tamano_de_lista)])

    (encontrado,iteraciones) = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f' el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista' )
    print(f' se hicieron {iteraciones} iteraciones')
