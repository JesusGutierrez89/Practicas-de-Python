#Recorrido y busqueda
L=[1,"Pepe", 5,7,"Hola"]
for c in L:
    print(c)
#For each
for i in range(4):
    print(i,L[i])

L2=[[0,1],[7],["hola",5 ,7]]
for i in range(len(L2)):
    for j in range(len(L2[i])):
        print("L2 es:",L2[i][j])

#List comprehension
L=[1,"Pepe", 5,7,"Hola"]
for i in range(11):
    L.append(i)
print(L)

#Busqueda de un elemento repetido 2 a mas veces
L4 =[1,5,7,3,5,7,8,9,3,2,3,6,5,8,10]
for i in range(len(L4)):
    print(L4[i])
x = int(input("Ingrese un numero a buscar 2 veces: "))
cont = 0
for i in range(len(L4)):
    if L4[i] == x:
        cont += 1
if cont == 2:
    print("El numero",x,"se repite 2 veces")
else:
    print("El numero",x,"se repite",cont,"veces")
    
#Busqueda de un elmento con un buble while (es la que se tiene que hacer)
L5 =[1,5,7,3,5,7,8,9,3,2,3,6,5,8,10]
cont = 0

y = int(input("Ingrese un numero a buscar 2 veces: "))
while (cont != 2 and i < len(L5)):
   
    if y == L5[i]:
        print(i)
        cont += 1
    i += 1
if cont == 2:
    print("El numero",y,"se repite 2 veces")
else:
    print("no se repite")
