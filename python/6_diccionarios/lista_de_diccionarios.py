""" 18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario
representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos
valores. Recorre la lista e imprime el nombre y edad de cada estudiante. """

estudiantes= [
    {"Nombre": "Juan", "Edad": "22"},
    {"Nombre": "Maria", "Edad": "25"},
]

for i in estudiantes:
    nombre = i ["Nombre"]
    edad = i ["Edad"]
    print("Nombre: ",nombre, "Edad: ",edad)

""" 19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las
mismas claves "nombre" y "edad". Imprime la lista actualizada. """

estudiantes.append({"Nombre": "Pedro", "Edad": "23"})

""" 20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada. """

del estudiantes[1]

""" 21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor.
Imprime la lista actualizada. """

estudiantes[0]["Edad"]= input("Cambia la edad del primer estudiante.")
print(estudiantes)