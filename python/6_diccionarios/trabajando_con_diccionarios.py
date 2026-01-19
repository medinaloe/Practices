""" 1. Crea un diccionario vacío llamado “mi_diccionario”. """

my_diccionario={ }

""" 2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor
sea tu nombre. """

my_diccionario["nombre"]="Enrique"

""" 3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario". """

print(my_diccionario["nombre"])

""" 4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False"
en caso contrario. """

print("edad" in my_diccionario)

""" 5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor:
"nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia
favorita. """
estudiante={
    "nombre":"juan",
    "edad": "15",
    "materia":"plastica",
}

""" 6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad
actual de tu amigo. """

estudiante["edad"]= "17"
print(estudiante)
""" 7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante". """

del estudiante["materia"]
print(estudiante)
""" 8. Imprime todas las claves en el diccionario “estudiante". """

for clave in estudiante:
    print(clave)
""" 9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor
"1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor
“5555555555”. """
agenda={
    "juan":"1234567890",
    "Joana":"9876543210",
    "Jimena":"5555555555",
}

""" 10.Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor
“9998887777". """

agenda["julio"]="9998887777"

""" 11.Imprime el número de entradas (pares clave-valor) en el diccionario “agenda". """

print(len(agenda))

""" 12.Crea una lista llamada "claves" que contenga todas las claves del diccionario
“agenda". """
claves=list(agenda.keys())
print(claves)

""" 13.Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y
"False" en caso contrario. """

print("juan" in agenda)

""" 14.Elimina la entrada con la clave “Jimena”. """

del agenda ["Jimena"]
print(agenda)
""" 15.Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e
imprime cada par clave-valor en el formato "Nombre: Número”. """

for nombre,numero in agenda.items():
    print(nombre + " : "+ numero)
 
""" 16.Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el
diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”. """

valor_juan = agenda.get("juan","Clave no encontrada")
print(valor_juan)

""" 17.Borra todas las entradas del diccionario “agenda”. """

agenda.clear()
print(agenda)