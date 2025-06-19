#Contar cuantas letras hay en en la palabra(diccionario)
def contar_caracteres(cadena):
    frecuencias = {}
    for char in cadena:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias

# Prueba
frase = input("Ponme una palabra: ")
frase = frase.replace(" ", "")
print(contar_caracteres(frase))

############################################
#Crear un diccionario con los cuadrados de los numeros desde 1 hasta n

def cuadrados(n):
    resultado = {}
    for i in range(1, n + 1):
        resultado[i] = i ** 2
    return resultado

numero = int(input("Dime un numero para calcular los cuadrados: "))
print(cuadrados(numero))

############################################
#Invertir un diccionario claves por valor
def invertir_diccionario(diccionario):
    diccionario_invertido = {}
    for clave, valor in diccionario.items():
        diccionario_invertido[valor] = clave
    return diccionario_invertido

diccionario = {"a": 1, "b": 2, "c": 3} #pone las claves como valores y los valores como claves
print(invertir_diccionario(diccionario))

############################################
#Filtar por edad
def filtrar_por_edad(diccionario, edad):
    resultado = {}
    for nombre, edad_persona in diccionario.items():
        if edad_persona >= edad:
            resultado[nombre] = edad_persona
    return resultado

personas = {"Juan": 25, "Maria": 18, "Pedro": 35, "Luis": 15}
edad = int(input("Dime una edad para filtrar: "))
print(filtrar_por_edad(personas, edad))

############################################
#Contar palabras

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.strip(".,!?").lower()
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

# Prueba
frase = input("Escribe una frase: ")
print(contar_palabras(frase))

############################################
#Dado un diccionario con nombres de productos y sus precios, encuentra el producto más caro.
def producto_mas_caro(diccionario):
    max_precio = max(diccionario.values())
    for producto, precio in diccionario.items():
        if precio == max_precio:
            return producto
        
productos = {"manzana": 2.5, "naranja": 3.2, "pera": 4.2, "uva": 5.2}
print(producto_mas_caro(productos))

############################################
#Dado un diccionario con nombres de productos y sus precios, calcula el precio total de la compra.
def sumar_ventas(lista_ventas):
    ventas_totales = {}
    for venta in lista_ventas:
        producto = venta['producto']
        cantidad = venta['cantidad']
        if producto in ventas_totales:
            ventas_totales[producto] += cantidad
        else:
            ventas_totales[producto] = cantidad
    return ventas_totales

# Prueba
ventas = [
    {'producto': 'manzana', 'cantidad': 10},
    {'producto': 'pera', 'cantidad': 5},
    {'producto': 'manzana', 'cantidad': 7},
    {'producto': 'pera', 'cantidad': 3}
]
print(sumar_ventas(ventas))

############################################

def promediar_calificaciones(dic1, dic2, dic3):
    promedios = {}
    
    # Unir todas las claves únicas de los tres diccionarios
    alumnos = set(dic1.keys()).union(dic2.keys(), dic3.keys())

    for alumno in alumnos:
        suma = 0
        contador = 0
        
        # Sumar calificaciones de los tres diccionarios si existen
        if alumno in dic1:
            suma += dic1[alumno]
            contador += 1
        if alumno in dic2:
            suma += dic2[alumno]
            contador += 1
        if alumno in dic3:
            suma += dic3[alumno]
            contador += 1
        
        # Calcular el promedio
        promedios[alumno] = suma / contador

    return promedios

# Prueba
parcial1 = {'Ana': 8, 'Pedro': 7, 'Luis': 9}
parcial2 = {'Ana': 9, 'Pedro': 8, 'Carlos': 7}
parcial3 = {'Ana': 9, 'Pedro': 8, 'Carlos': 7}

print(promediar_calificaciones(parcial1, parcial2, parcial3))