#a partir de una cadena se crea una lista con las palabras
frase=str(input("Dime una frase para poder recogerla en una lista: "))
lista = frase.split(" ")
print(lista)

#contar palabras
def contarPalabras(lista):
    cont = 0
    for palabra in lista:
        cont = cont + 1
    return cont

#palabra mas larga
def palabraMasLarga(lista):
    palabraLarga = ""
    for palabra in lista:
        if len(palabra) > len(palabraLarga):
            palabraLarga = palabra
    return palabraLarga

#palabra mas corta
def palabramasCorta(lista):
    palabraCorta = len(palabra)
    for palabra in lista:
        if len(palabra) < len(palabraCorta):
            palabraCorta = palabra
    return palabraCorta

print(f"El numero de palabras es: {contarPalabras(lista)}")
print(f"La palabra mas larga es: {palabraMasLarga(lista)}")
print(f"La palabra mas corta es: {palabramasCorta(lista)}")



