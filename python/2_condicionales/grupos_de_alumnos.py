"""En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
pantalla el grupo que le corresponde a ese alumno."""

genero = str (input("¿Eres chico o chica? "))
                    

if genero.lower() == "chica":
 nombre_chica = str (input("Escriba su nombre: "))
else:
 nombre_chico = str (input("Escriba su nombre: "))

# SI EL NOMBRE ES DE CHICA
if "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" in nombre_chica[0].lower():
 print (nombre_chica.title(), " estas en el grupo A")
else:
   print (nombre_chica.title(), " estas en el grupo B")

#SI EL NOMBRE ES DE CHICO
   if "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" in nombre_chico[0].lower():
      print (nombre_chico.title(), " estas en el grupo A")
   else:
       print (nombre_chico.title(), " estas en el grupo B")
 
