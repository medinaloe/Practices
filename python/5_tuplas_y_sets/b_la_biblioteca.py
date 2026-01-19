
""" Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista 
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del 
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del 
libro y el apellido del autor. """
 #Pista: Tus datos de entrada podrían ser así  —> lista_libros = [(‘El aleph', ‘Jorge Luis 
#Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros', 
#‘Mario Vargas Llosa')]

lista_libros = [("El aleph", "Jorge Luis Borges"), ("Cien años de soledad", "Garbriel Garcia Márquez"), ("La ciudad y los perros", "Mario Vargas Llosa")]
titulo_apellido=[]

for i in lista_libros:
    titulo, autor= i
    apellido= autor.split()[-1]
    titulo_apellido.append((titulo,apellido))
titulo_apellido=tuple(titulo_apellido)
print(type(titulo_apellido))
print(titulo_apellido)
    