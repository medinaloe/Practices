""" 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una 
nueva linea. """
print("Ejercicio1:")
print()
tupla = (23, "Hola", False)
for i in tupla:
    print(i)
print()


"""  3. Crea una tupla de enteros y devuelve la suma de los elementos. """
print("Ejercicio3:")
print()
tupla_enteros= (1,2,3,4)
suma= sum(tupla_enteros)
print(suma)
print()

"""  4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el 
primer caracter de cada string. """
print("Ejercicio4.")
tupla=("hola","adios","platano","fresa")
lista=[]
for i in tupla:
    lista.append(i[0])
tupla2= tuple(lista)
print(tupla2)
print()

"""  5. Crea un script que dada una tupla de números devuelva el producto de todos los 
números pares.  """
print("Ejercicio5:")
tupla= (1,2,3,4,5,6,7,8,9,10)
lista_pares=[]
for i in tupla:
    if i % 2 == 0:
     lista_pares.append(i)
print(lista_pares)
print()
""" 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros 
ordeandos en orden descendente. """
print("Ejecicio6")
tupla=(2,5,6,8,3,4,2,9,80,44)
tupla_ordenada= tuple(sorted(tupla))
tupla_descendente= tuple(reversed(tupla_ordenada))
print(tupla_descendente)
print()
""" 7. Crea un script que dada una tupla con números enteros repetidos, elimine los 
duplicados. (Puedes usar sets). """
print("Ejercicio7:")
tupla=(1,1,1,2,2,3,3,4,4)
set = set(tupla)
tupla2 = tuple(set)
print(tupla2)
print()

""" 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el 
numero se encuentra en la tupla y falso en el caso contrario. """
print("Ejercicio8:")

tupla= (1,2,4,6,7,44,55,32,77)
target=5
comprobar= target in tupla
print(comprobar)
print()


""" 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas. """
print("Ejercicio9:")
tupla1=(1,2,3)
tupla2=(4,5,6)
union_tuplas= tupla1+tupla2
print(union_tuplas)
print()
"""  10. Crea un script que dada una tupla de números devuelva e máximo y el mínimo. """
print("Ejercicio10:")
tupla=(3,4,7,1,8,9)
maximo= max(tupla)
minimo=min(tupla)
print(maximo,minimo)
print()
"""  11. Crea un script que dada una tupla con strings devuelva el string más largo y el más 
corto. (Prueba añadiendo key=len a las funciones max y min). """
print("Ejercicio11:")
tupla= ("Manzana","Pera","Zanaoria","Sandia","Maracuya")
maximo=max(tupla,key=len)
minimo=min(tupla,key=len)
print(maximo,minimo)
print()
""" 12. Crea un script que dada una tupla devuelva el contenido en orden revertido. """
print("Ejercicio12:")
tupla= ("Manzana","Pera","Zanaoria","Sandia","Maracuya")
revertida= tuple(reversed(tupla))
print(revertida)
print()
 
""" 13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos 
elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos 
elementos de la tupla interna correspondiente. """
print("Ejercicio13:")
tupla= ((1,2),(4,5),(7,8))
lista=[]
for i in tupla:
    suma=sum(i)
    lista.append(suma)
tupla2 = tuple(lista)
print(tupla2)
