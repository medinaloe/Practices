""" 22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada
representa un producto y tiene a su vez las claves "nombre" y "precio" con sus
respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada
producto. """
productos= {
    "producto1": {"Nombre": "Platano", "Precio": "2"},
    "producto2": {"Nombre": "Manzana", "Precio": "3"},
}
for i ,costo in productos.items():
    nombre = costo ["Nombre"]
    precio = costo ["Precio"]
    print("Nombre: ",nombre, "Precio: ",precio)
    
""" 23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y
valor. Imprime el diccionario actualizado. """

productos["producto3"]= {"Nombre": "Pera", "Precio": "5"}
print(productos)

""" 24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada
representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de
los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de
jugadores. """

equipos= {
    "equipo1": {"Nombre": "Betis", "Jugadores": ["Juan","Pedro", "Javier"]},
    "equipo2": {"Nombre": "Depor", "Jugadores": ["Manquillo","Valeron","Marchena"]},
    "equipo3": {"Nombre": "Gijon", "Jugadores": ["Villa", "Canella","Stuani"]},
}

for equipo ,jugador in equipos.items():
    nombre = jugador ["Nombre"]
    futbolistas = jugador ["Jugadores"]
    print("Nombre equipo: ",nombre, "Jugadores: ",futbolistas)

""" 25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario
actualizado. """

equipos["equipo4"]= {"Nombre": "Atleti", "Jugadores": ["Costa", "Filipe","Godin"]}
print(equipos)

""" 26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario
"equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado. """

equipos["equipo1"]["Jugadores"].append("Isco")
print(equipos)