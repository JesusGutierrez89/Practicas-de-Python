import random

### CONSTRUIR LA MATRIZ ###
def mezclar(frase):
    # Para construir la matriz cuadrada
    longitud = len(frase)

    # Eliminamos espacios
    fraseSinEsps = frase.replace(" ","")

    matriz = list()

    for i in range(longitud):
        matriz.append([])
        for j in range(longitud):
            matriz[i].append(fraseSinEsps[random.randint(0, len(fraseSinEsps)-1)])

    return matriz

### MOSTRAR LA MATRIZ ###
def mostrarMezcla(matriz):
    for F in matriz:
        lista = list()
        for C in F:
            lista.append(C)
        print(' - '.join(lista)) # Así controlamos no mostrar la separación en el último elemento

## COMPROBAR MISMO VALOR EN LAS 3 FILAS ##
def comprobarRepetidos(matriz, dic):
    
    for caracter in matriz[0]:
        # Si la letra ya está en el diccionario registrada, no hay que volver a ejecutar la búsqueda (para letras repetidas en la misma fila)
        if caracter not in dic:
            caracterEnTodasLasFilas = True # Seguimos con la búsqueda hasta que alguna fila no tenga el valor (no tiene sentido seguir)
            numFila = 1 # Porque de la fila 0 obtenemos los valores a buscar
            ultFila = len(matriz)

            while(caracterEnTodasLasFilas == True and numFila < ultFila):
                if(caracter not in matriz[numFila]):
                    caracterEnTodasLasFilas = False
                numFila += 1
        
            # Al salir del bucle, comprobamos si la salida ha sido debido a que no está el carácter en todas las filas
            if(caracterEnTodasLasFilas == True):
                dic[caracter] = True
        


### MAIN ###
frase = input("Introduce una frase: ")
matriz = mezclar(frase)
mostrarMezcla(matriz)

repetidas = dict()
comprobarRepetidos(matriz, repetidas)

print("")

## EVALUAR RESULTADO DE LA BÚSQUEDA EN MAIN ##
resultado = len(repetidas)
if(resultado == 0):
    print("No hay ninguna letra que se repita en todas las filas")
elif(resultado == 1):
    listaClaves = list(repetidas.keys())
    print(f"Hay una letra que se repite: {listaClaves[0]}") # Únicamente hay 1 clave

else:
    print(f"Hay {resultado} letras que se repiten: ", end="")
    for letra in list(repetidas.keys()):
        print(letra, end=" ")
    
print("")