# 1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas -\ 
# de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa

frutas=["manzana","platano","cereza","pera","higo","frambuesa","higo"]

#2. Usa la función len() para imprimir la longitud de la lista frutas.

print (len(frutas))
print(" ")
#3.Accede al objeto numero 3 de la lista e imprímelo or consola. 

print (frutas[2])

#4. Modifica el segundo objeto de la lista y cambiado a mora.
frutas [1]="mora"

#5. Añade el string mango al final de la lista.

frutas.append("mango")

#36. Usa el método insert() y añade el string “uva“ año comienzo de la lista.

frutas.insert(0, "uva")

#7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola

print(" ")
for i in frutas:
    print(i)

#8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
 #llamada “ultima_fruta“
  
ultima_frutas= frutas.pop(-1)

#9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola

print(" ")
for i in frutas:
    print(i)

#10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola

print("")
for i in frutas:
    longitud_fruta = len(i)
    print(longitud_fruta)

#11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
#tengan más de 5 caracteres

print("")
for i in frutas:
    longitud_fruta = len(i)
    if longitud_fruta >= 5:
        print(i)

#12. Usa el método remove() para borrar el string “cereza“ de la lista.

frutas.remove("cereza")

#13. Usa el método clear() para vaciar la lista. 
print(" ")
frutas.clear()
print(frutas)