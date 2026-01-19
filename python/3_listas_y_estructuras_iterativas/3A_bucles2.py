""""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. """""

password = str("contraseña")
contraseña = " "

while contraseña != password:
        contraseña = input ("Escribe la contraseña: ")
        if contraseña != password:
                input ("La contraseña no es correcta, escribala de nuevo: ")
print("La contraseña es correcta.")
        
