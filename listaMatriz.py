# Crea un programa que permita generar y mostrar una tabla dinámica de datos utilizando listas.

# Solicita al usuario el número de filas y columnas que tendrá la tabla.
# Llena la tabla con números aleatorios entre 1 y 100 utilizando bucles.
# Permite al usuario realizar las siguientes operaciones:
# Imprimir la tabla completa.
# Calcular la suma de una fila específica.
# Calcular la suma de una columna específica.
# Encontrar el valor máximo y mínimo de toda la tabla.
import random

#Rellenar tabla
def crearTabla():
    numColumna = int(input("Dime el numero de columnas: "))
    numFila = int(input("Dime el numero de filas: "))
    tablaDinamica=[]

    for i in range(numFila):
        fila=[]
        for j in range(numColumna):
            fila.append(random.randint(1,100))
        tablaDinamica.append(fila)
    return tablaDinamica
#Mostrar tabla
def mostrarTabla(tablaDinamica):
    print("Matriz:")
    for fila in tablaDinamica:
        print(fila)

#Calcular la suma de una columna específica.
def sumaColumna(matriz,numColumna):
    suma = 0
    for fila in matriz:
        suma += fila[numColumna]
    return suma

#Encontrar el valor máximo y mínimo de toda la tabla.
def valorMaxMin(matriz):
    max = matriz[0][0]
    min = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > max:
                max = elemento
            if elemento < min:
                min = elemento
    return max, min

# Crear y mostrar la tabla
tabla = crearTabla()
mostrarTabla(tabla)

# Pedir al usuario la columna y mostrar la suma
columna = int(input("Dime el número de la columna para sumar: "))
print(f"La suma de la columna {columna} es: {sumaColumna(tabla, columna)}")

# Mostrar el valor máximo y mínimo de la tabla
max_val, min_val = valorMaxMin(tabla)
print(f"El valor máximo de la tabla es: {max_val}")
print(f"El valor mínimo de la tabla es: {min_val}")  

        
