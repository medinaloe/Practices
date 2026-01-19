""" Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase.  """
#Ejercicio empezado por mi pidiendo las notas por el programa, hecho como en clase en la parte 2.

alumnos = (["Maria", "Juan", "Pedro","Jessi"])
database =[]

for i in alumnos:
    notas=[]
    print("Ingresa las notas del estudiante",i)
    deberes = float (input("Nota de los deberes "))
    notas.append(deberes)
    examenes = float (input("Nota de los examenes "))
    notas.append(examenes)
    proyectos = float (input("Nota de los proyectos "))
    notas.append(proyectos)
    database.append((i,notas))


#Parte 2 ejercicio hecho como en la clase.

for data in database:
    nombre = data[0]
    notas = data[1]
    media = sum(notas) / len(notas)
    print (f"La media de {nombre} es de {media :.2f}")

#Nota media de toda la clase.

total_notas= 0
num_notas = 0

for data in database:
    notas = data[1]
    total_notas = total_notas + sum(notas)
    num_notas = num_notas + len(notas)

media_clase= total_notas/num_notas
print(f"La media de la clase es de {media_clase:.2f} .")

# f"    " {media_clase:.2f} ----> me redondea los resultados que aparecen de las operaciones a 2 digitos despues de la coma (,)

