""" Crea un array_1 lleno ceros con una longitud de 8 elementos.  """

import numpy as np
arrays1= np.array([0,0,0,0,0,0,0,0])
print(arrays1)

""" Haz que todos los elementos de este array sean igual a 2  """

arrays1 [:]=2
print("array cambiado", arrays1)

""" Crea un array_2 que contenga todos los números pares del 1 al 10. """

import numpy as np
array_2 = np.arange(2,11,2)
print(array_2)

""" Suma todos los elementos del array_2 usando un bucle y después usando un método
de numpy. Compara los resultados """

suma_bucle= 0
for i in array_2:
    suma_bucle =  suma_bucle + i
print("suma de modo bucle", suma_bucle)

suma_nuevometodo = np.sum(array_2)
print("suma metodo nuevo", suma_nuevometodo)

""" Revierte array_2 y guárdalo en una variable independiente. """

array_2_inverso= array_2[::-1]
print("array inverso", array_2_inverso)

""" Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y
array_2_revertido
 (Pista: Investiga el uso de intersect1d() de numpy) """
 
comun1 = np.intersect1d(arrays1,array_2)
print("numeros en comun entere el array 1 y el array 2", comun1)
comun2= np.intersect1d(array_2,array_2_inverso)
print("numeros en comun entere el array 2 y el array 2 inverso", comun1)

""" Crea un arrays lleno de 1s con una longitud dada por el usuario """

import numpy as np
longitud= int(input("Introduzca la longitud del array:"))
array_elegir= np.ones(longitud)
print(array_elegir)

