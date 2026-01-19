#1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:[1,2,3,4,5,6,7,8,9,10].

numeros = [1,2,3,4,5,6,7,8,9,10]

#2. Crea una nueva lista con los números pares de la lista anterior en orden inverso

numeros_pares = list (range(2,11,2))
numeros_pares.reverse()
print (numeros_pares)

#3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero porconsola.

print(" ")
for i in numeros:
 i = i **2
 print(i)

#4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método decompresión).

#5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
print(" ")
minimo = min(numeros)
print (minimo)
#6. Haz lo mismo con el número más alto
print(" ")
maximo=max(numeros)
print(maximo)

#7. Suma todos los elementos de la lista con y sin un bucle.
print(" ")
suma = 0
for num in numeros:
 suma = suma + num

print (suma, "Es el resultado de la suma de todos los numeros")

suma =sum(numeros)
print(suma,"Es el resultado de la suma de todos los numeros sin bucle")
#8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante trasel punto 2
original = numeros.index(8)
invertida = numeros_pares.index(8)
print(original)
print(invertida)