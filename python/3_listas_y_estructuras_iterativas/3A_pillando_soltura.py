#1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
#añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
#elementos únicos.

lista = (1,2,3,4,5,3,4,5,6,7,8,8,9,10) 
duplicados =[]
unicos =[]
for i in lista :
    if lista.count(i) > 1:
        if i not in duplicados:
            duplicados.append(i)
    else:
        unicos.append(i)
print(lista, " Lista original")
print (unicos, " Son los elementos unicos.")
print(duplicados, " Son los elementos duplicados")
    
#2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.

lista1 =  [1,2,3,5,7,8,9,10]
lista2 = [6,8,13,14,11]

lista_ascendente = lista1 + lista2
lista_ascendente.sort()
print(lista_ascendente, " Lista ascendente")

#3. Escribe un script que encuentre el segundo número más grande de una lista.
lista3 = [2,3,6,8,9,5,10,7]
lista3.sort()
print ("El segundo numero más alto de la lista 3 es ", lista3 [-2])

#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).

lista4 = [2,3,5,6,7,8,9]
num = int  (input ("Escriba un numero: "))
contador = int()
for p in lista4:
    if p > num:
       contador = contador + 1

print(contador)

#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este.
lista5= (3,4,1,5,6,2,7,8)
num_usu = int (input("Escribe un numero: "))
suma= int()
for n in lista5:
    if n % num_usu == 0 :
       suma = suma + n
print(suma)

#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.

numeros =[3,4,5,6,7,8,9,0]
num = int (input("Pon un numero: "))
numeros.sort()
for i in numeros:
    if i < num:
        resultado = i
print (resultado)  

#7. Crea un script que extraiga los elementos comunes entre dos listas.

lista1= [1,2,3,4,5,6,7,8,9]
lista2= [2,3,6,8,9]
lista_comun = []
for i in lista1:
    if i in lista2:
        lista_comun.append(i)


print(lista_comun)
#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)

lista = [4,5,4,5,4,57,8,9,6,5,7,4,1,2,3,6]
apariciones = []
for i in lista:
   print("El elemento", i , "aparece", lista.count(i), " en la lista.") 


#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
#números positivos de la lista original.

lista_original= [1,2,-2,-3,-4,-5,-8,9,7]
lista_positivos= []

for i in lista_original:
    if i > 0:
        lista_positivos.append(i)
print (lista_positivos)

#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.

lista_string = ["hola", "adios", "vale", "como"]
lista_longitud = []
for i in lista_string:
    longitud = 0
    for d in i:
        longitud = longitud +1
    lista_longitud.append(longitud)

print(lista_longitud)

#11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en mayúscula. 

lista_string = ["hola", "adios", "vale", "como"]
lista_mayusculas= []

for string in lista_string :
    lista_mayusculas.append(string.upper())
print(lista_mayusculas)