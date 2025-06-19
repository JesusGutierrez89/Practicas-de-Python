# Creación de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

#Acceso a elementos de una matriz
# Acceder al elemento en la fila 1, columna 2
elemento = matriz[0][1]  # Resultado: 2

#Iterar sobre las filas y columnas
for fila in matriz:
    for columna in fila:
        print(columna)


# Transponer una matriz
matriz_transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(matriz_transpuesta)

#Sumar Matrices
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

matriz_suma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print(matriz_suma)

#Multiplicar Matriz
escala = 2
matriz_multiplicada = [[elemento * escala for elemento in fila] for fila in matriz]
print(matriz_multiplicada)

#Creación de un diccionario
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

#Acceder a los valores de un diccionario
nombre = diccionario['nombre']  # Resultado: 'Juan'
edad = diccionario['edad']      # Resultado: 25

# Modificar un valor
diccionario['edad'] = 26

# Añadir un nuevo valor
diccionario['profesion'] = 'Ingeniero'


# Iterar sobre las claves
for clave in diccionario:
    print(clave)

# Iterar sobre las claves y valores
for clave, valor in diccionario.items():
    print(clave, valor)


# Eliminar una clave
del diccionario['profesion']

# Usar pop para eliminar una clave y obtener su valor
edad = diccionario.pop('edad')


#Comprobar si una clave existe
if 'nombre' in diccionario:
    print('La clave "nombre" está en el diccionario')



# Diccionario con matrices
matrices_diccionario = {
    'matriz1': [[1, 2], [3, 4]],
    'matriz2': [[5, 6], [7, 8]]
}

# Acceder a una matriz
print(matrices_diccionario['matriz1'])

#Alamcenar Resultado
resultados = {
    'suma': matriz_suma,
    'producto': matriz_multiplicada
}


#Crear matriz a partir de filas y columnas 
def crear_matriz(filas, columnas):
    # Crear una matriz de ceros con las dimensiones dadas
    # el guion bajo sirve si el indice no te interesa
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz

# Ejemplo de uso
filas = 3
columnas = 4
matriz = crear_matriz(filas, columnas)

for fila in matriz:
    print(fila)


#Mostrar Matriz 

def mostrarMatriz(matriz):
    for f in matriz:
        print("", end="\t")
        for e in f:
            print(e, end="\t")
        print("\n")

# Rango con parámetros
for i in range(2, 10, 2):
    print(i)
    


# lista[inicio:fin:paso]
# inicio: El índice donde empieza el corte (inclusivo). Si se omite, empieza desde el inicio.
# fin: El índice donde termina el corte (exclusivo). Si se omite, llega hasta el final de la lista.
# paso: El intervalo entre los elementos a seleccionar. Si se omite, el valor predeterminado es 1.    

# Lista original
lista = [0, 1, 2, 3, 4, 5]

# Reemplazamos los elementos de índice 2 a 4 (no incluye 4) por nuevos valores
lista[2:4] = [10, 11, 12]

print(lista)

# Lista original
lista = [0, 1, 2, 3, 4, 5]

# Eliminamos los elementos de índice 2 a 4
lista[2:5] = []

print(lista)

# Lista original
lista = [0, 1, 2, 3, 4, 5]

# Insertamos los elementos [100, 101] en el índice 2
lista[2:2] = [100, 101]

print(lista)

# Lista original
lista = [0, 1, 2, 3, 4, 5]

# Eliminamos 3 elementos comenzando en el índice 2
del lista[2:5]

print(lista)

lista = [0, 1, 2, 3, 4, 5]
sublista = lista[:3]  # Toma desde el inicio hasta el índice 2 (excluido)
print(sublista)  # [0, 1, 2]

lista = [0, 1, 2, 3, 4, 5]
sublista = lista[2:]  # Toma desde el índice 2 hasta el final
print(sublista)  # [2, 3, 4, 5]

lista = [0, 1, 2, 3, 4, 5]
sublista = lista[::2]  # Toma cada 2 elementos
print(sublista)  # [0, 2, 4]

lista = [0, 1, 2, 3, 4, 5]
sublista = lista[::-1]  # Invierte la lista
print(sublista)  # [5, 4, 3, 2, 1, 0]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista = lista[1:8:2]  # Toma los elementos de índice 1 a 7 con paso 2
print(sublista)  # [1, 3, 5, 7]

lista = [0, 1, 2, 3, 4, 5]
sublista = lista[-3:-1]  # Toma los elementos desde el índice -3 hasta -2 (sin incluir el -1)
print(sublista)  # [3, 4]

#Diccionario dentro de Diccionario
diccionario = {
    "clave1": {
        "subclave1": valor1,
        "subclave2": valor2
    },
    "clave2": {
        "subclave1": valor3,
        "subclave2": valor4
    }
}


# Crear un diccionario vacío
diccionario = {}

# Lista de claves
claves = ["nombre", "edad", "ciudad"]

# Usar un bucle para pedir los valores
for clave in claves:
    valor = input(f"Ingrese el valor para {clave}: ")
    diccionario[clave] = valor

print(diccionario)


# Lista de estudiantes y materias
estudiantes = ["Juan", "María", "Pedro"]
materias = ["Matemáticas", "Historia", "Ciencias"]

# Crear un diccionario vacío
diccionario = {}

# Usamos un bucle para crear un diccionario dentro de otro
for estudiante in estudiantes:
    # Crear un subdiccionario para cada estudiante
    calificaciones = {}
    for materia in materias:
        # Pedir la calificación para cada materia
        calificacion = input(f"Ingresa la calificación de {estudiante} en {materia}: ")
        calificaciones[materia] = calificacion
    
    # Asignar el subdiccionario al estudiante
    diccionario[estudiante] = calificaciones

print(diccionario)