"""El objetivo de este ejercicio es que crees un script que dado un nombre de usuario le de la
bienvenida con su nombre en el formato correcto."""

"""1. Escribe un programa que almacene el string ‘estas usando python’ en una variable y luego
muestre por pantalla el contenido de la variable"""

mensaje = "Estas usando python"
print (mensaje) 

"""2. Amplía el programa para que pregunte el nombre de usuario en la terminal y después muestre
por pantalla el mensaje: ‘¡Hola, <nombre>, estas usando python! (<nombre> es el nombre que
el usuario hay introducido)"""

print ("¡Hola!, ¿Cual es tu nombre de usuario?")
nombre = input()

"""3. Usa una función interna de python que actúe sobre el string que has creado antes para que el
mensaje que imprima sea: ‘¡HOLA, <NOMBRE>, ESTAS USANDO PYTHON!"""

mensaje2 = ("¡Hola " + nombre + " estas usando python!")
print (mensaje2)

"""4. Cambia el script para que el mensaje se imprima al completo en minúsculas (usa de nuevo
una función interna de python)"""

#MENSAJE EN MAYUSCULAS
print (mensaje2.upper())

"""5. Cambia el script para que, sin importar como introduzca el usuario el nombre, lo formatee para
que tenga el formato correcto, es decir con la primera letra en mayúsculas y las demás en
minúscula (Si el usuario introduce el nombre ferNanDO, el programa deberá formatear el
nombre a Fernando)"""

#MENSAJE EN MINUSCULAS
print (mensaje2.lower())

"""6. Amplía el script para que si por error el usuario introduce un nombre con un punto en medio, el
programa automáticamente lo borre (Si el usuario introduce el nombre Fern.ando, el programa
deberá formatear el nombre a Fernando)"""

# MENSAJE SE ESCRIBE MAYUSCULA SOLO LA PRIMERA DESPUES DE CADA ESPACIO O PUNTO
print (mensaje2.title())

"""7. Consigue que el mensaje final sea: ‘¡Hola, <Nombre>, estas usando Python!"""

# En este caso elimina si hay puntos en el nombre haciendo que aparezca bien por completo
print (mensaje2.replace(".",""))
