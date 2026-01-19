""" Crea un array con 15 números enteros aleatorios entre 1 y 100 """

import numpy as np
array_azar = np.random.randint(1,101,size=15)
print(" El array escrito al azar es: ", array_azar)

""" Multiplica todos los elementos del array usando un bucle y después usando un
método de numpy. Compara los resultados """

multiplicacion_bucle = 1
for i in array_azar:
    multiplicacion_bucle= multiplicacion_bucle * i
print (" La multiplicacion usando el bucle da: ", multiplicacion_bucle)

multiplicacion_numpy= np.prod(array_azar)
print(" La multiplicacion usando el metodo numpy da: ", multiplicacion_numpy)

"""Crea otro array con 15 números decimales aleatorios entre 0 y 1 """

import numpy as np
array_azar2 = np.random.uniform(1.0,101.0,size=15)
print(" El segundo array con decimales escrito al azar es: ", array_azar2)

"""Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
operador y después con una función de numpy
 (Pista: busca en google que función de numpy hace esto) """

suma_array = array_azar + array_azar2
print("Suma de arrays con metodo normal : ",suma_array)
suma_numpy = np.add(array_azar,array_azar2)
print("Suma listas de arrays metodo numpy : ",suma_numpy)

""" Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
(Pista: busca en google que función de numpy hace esto) """

resta_array = array_azar - array_azar2
print("Resta de arrays con metodo normal : ",resta_array)
resta_numpy = np.subtract(array_azar,array_azar2)
print("Resta listas de arrays metodo numpy : ",resta_numpy)

""" Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
después con una función de numpy
 (Pista: busca en google que función de numpy hace esto) """
 
multi_array = array_azar - array_azar2
print("Multiplicaion de arrays con metodo normal : ",multi_array)
multi_numpy = np.multiply(array_azar,array_azar2)
print("Multiplicacion de listas de arrays metodo numpy : ",multi_numpy)

"""Encuentra el valor más alto del primer array que has creado. """

valor_alto= np.max(array_azar)
print("El valor mas alto del primer array es: ",valor_alto)

""" Calcula la media (mean), la mediana (median) y al deviación estandar (standard
deviation) de los arrays (Nota: No nos importa el significado matemático de estos
valores, lo importante es que encuentres que función de numpy necesitas. Puedes
hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
haber más resultados). """

media= np.mean(array_azar)
print("La media del array es :",media)

mediana= np.median(array_azar)
print("La mediana del array es :",mediana)

deviacion_estandar= np.std(array_azar)
print("La deviacion estandar del array es :", deviacion_estandar)