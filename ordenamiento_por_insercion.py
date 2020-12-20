import random 

n = int(input("por favor ingrese el tamaño de la lista"))

lista= ([random.randint(0,100) for i in range (n)])
lista2= lista[0]
lista = lista.pop(0)
for i in range (n):
    if lista[i]>lista2[i]:
        lista2.append()


print(lista)
