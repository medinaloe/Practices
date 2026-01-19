""" Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas)  """

asistencias={}
#registro de asistencias
asistencias["Juan"]=["05-09-2020","06-09-2020","08-09-2020"]
asistencias["Pepe"]=["05-09-2020","07-09-2020","08-09-2020"]
asistencias["Jose"]=["04-09-2020","05-09-2020","08-09-2020"]

#nuevas asistencias
asistencias["Jose"].append("09-09-2020")
asistencias["Juan"].append("10-09-2020")
print(asistencias)
#lista de asistencia de estudiantes

for estudiante, asistencia in asistencias.items():
    print("Estudiante:",estudiante)
    print("Asistencias:"," , ".join(asistencia))
