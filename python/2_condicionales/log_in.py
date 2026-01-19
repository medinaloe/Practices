"""Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas."""

contraseña = "password"

contraseña = input ("Escriba su contraseña: ")

if contraseña.lower == "password":
     print ("Bienvenido de nuevo usuario.")
else: 
     print ("La contraseña no es correcta, intentelo de nuevo: ")
     contraseña= input()
     if  contraseña.lower == "password":
          print ("Bienvenido de nuevo usuario.")
     else:
          print ("La contraseña no es correcta, tiene un ultimo intento: ")
          contraseña = input()
          if contraseña.lower == "password":
            print ("Bienvenido de nuevo usuario.")
          else: 
              print ("Ha habido un error con la autentificacion de su contraseña. ")