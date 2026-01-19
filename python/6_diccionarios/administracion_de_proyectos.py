""" Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de diccionarios) """

tareas={}
#agregar tareas
tareas["Tarea1"]= {"Descripcion":"Encargado de mantenimiento","Responsable":"Juan"}
tareas["Tarea2"]= {"Descripcion":"Limpieza","Responsable":"Raul"}
tareas["Tarea3"]= {"Descripcion":"Administrador","Responsable":"Marta"}
#Asignar responsables a las tareas existentes
tareas["Tarea1"]["Responable"]= "Javi"
#Cambiar descripcion  a las tareas existentes
tareas["Tarea2"]["Descripcion"]= "Cuenta puntos"
#lista de tareas
for tarea,responsable in tareas.items():
    print(tarea,responsable)