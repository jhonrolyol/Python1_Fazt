
myStr = "Hello World"

# print(dir(myStr))

print(myStr.upper()) # Muestra en Mayuscula.
print(myStr.lower()) # Muestra en Minuscula.
print(myStr.swapcase()) # Muestra la primera letra de una palabra en Minuscula.
print(myStr.capitalize()) # La primera letra en Mayuscula y resto en Minuscula.

print(myStr.replace('Hello', 'Bye')) # Cambia y remplaza.
print(myStr.replace('Hello', 'Bye').upper()) # Cambia y remplaza todo en Mayuscula.

# Contar la cantidad de "l" en "myStr".
print(myStr.count('l'))

# Contar la cantidad de "o" en "myStr".
print(myStr.count('o'))

# Contar la cantidad de " " en "myStr".
print(myStr.count(' '))

# Ver la palabra que inicia en "myStr" con "startswith".
print(myStr.startswith('hola')) # Resultado puede ser True o False.
print(myStr.startswith('H')) # Resultado puede ser True o False.
print(myStr.startswith('He')) # Resultado puede ser True o False.


# Ver la palabra que termina en "myStr" con "endswith".
print(myStr.endswith('World')) # Resultado puede ser True o False.
print(myStr.endswith('world')) # Resultado puede ser True o False.

# Dividir un caracter con "split".

myStr = "Hello World Car"
print(myStr.split()) # Separa a partir de un caracter vacio.

myStr = "Hello, World, Car"
print(myStr.split(',')) # Separa a partir de una coma.

myStr = "Hello, World, Car"
print(myStr.split('o')) # Separa a partir de una coma.

# Busca la posición de la letra "o" en "myStr".
print(myStr.split('o')) 
print(myStr.split(' ')) 

myStr = "Hello Worldz"
print(myStr.split('z')) 

# Tamaño del string. 
print(len(myStr))

# Índice de una palabra. 
print(myStr.index('e'))

# Ver si es numérico. 
print(myStr.isnumeric())

# Ver si es alpha numérico.
print(myStr.isalpha())

# Imprimir la posición.
myStr = "Hello World" 
print(myStr[5])
print(myStr[0])
print(myStr[3])
print(myStr[4])

print(myStr[-1]) # Orden inverso. 
print(myStr[-5]) # Orden inverso.

# Concatenación
myStr = "Hello World"
print("El saludo clásico en programación es:  " + myStr)
print(f"El saludo clásico en programación es: {myStr}")
print("El saludo clásico en programación es: {0}".format(myStr))


# Note: 
# Comentario de multiples líneas: Control + shiff + P + comment

