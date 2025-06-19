#Dame el tamaño de una lista con el usuario, despues que se rellene a la lista de 0 - 100

import random


num = int(input("Dame el tamaño de la lista: "))
lista = []  

#Mostrar una lista con guiones y un espacio al final (Forma marrana)
for i in range(num):
    lista.append(random.randint(0, 100))
    
for i in range(num):
    if i == num - 1:
        print(lista[i], end = " ")
    else:
        print(lista[i], end = "-")

#Forma correcta de mostrar la lista con el espacio al final

num1 = int(input("Dame el tamaño de la lista: "))
lista1 = []  
resultado = ""

for e in range(num1):
    lista1.append(random.randint(0, 100))
    
for e in range(num1):
    resultado += str(e) + " - "
print(resultado[:-3])
