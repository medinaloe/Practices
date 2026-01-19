""" 14.Crea un set y elimina uno de sus elementos. """
print("Ejercicio14:")
my_set= {1,2,3,4}
my_set.discard(2)
print(my_set)
print()
"""  15.Crea un set vacío. """
print("EJercicio15:")
my_set = set()
print(my_set)
""" 16.Crea dos sets y encuentra su union, su intersección y su diferencia. """
print("Ejercicio16: ")
set1= {1,2,3}
set2={3,4,5}
print("La union es: ",set1.union(set2))
print("La interseccion es: ",set1.intersection(set2))
print("La diferencia es: ",set1.difference(set2))
print()
""" 17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos 
comunes de ambos. """
print("Ejercicio17:")
set1={1,2,3,5,7,8}
set2={4,5,7}
set_comun = (set1 & set2)
print(set_comun)
print(type(set_comun))
print()
"""  18.Crea un script que dado un set con números devuelva el numero máximo y mínimo. """
print("Ejercicio18:")
my_set={3,4,6,8,2,5,9,8,1}
minimo=min(my_set)
maximo=max(my_set)
print(maximo,minimo)
print()
""" 19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de 
cada uno de los sets. """
print("Ejercicio19:")
set1={1,2,3,5,7,8}
set2={4,5,7}
print(set1.symmetric_difference(set2))
print()
"""  20.Crea un set con colores y comprueba si cierto color se encuentra en el set. """
print("Ejercicio20")
my_set={"azul","morado","verde","negro"}
pertenencia = "amarillo" in my_set
print(pertenencia)
print()
""" 21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en 
el primer set pero no en el segundo. """
print("Ejercicio21:")
set1={1,2,3,5,7,8}
set2={4,5,7}
set3= set1.difference(set2)
print(set3)
print()
"""  22.Crea un script que dado un set de enteros devuelva el producto de todos los números 
dentro del set.  """
print("Ejercicio22:")
set1={1,2,3,5,7,8}
producto=1
for i in set1:
    producto=producto* i
print(producto)