""" Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto)  """
#Dic.de ventas
registro_de_ventas= {}
#registro de productos y cantidades
registro_de_ventas["producto1"]=5
registro_de_ventas["producto2"]=7
registro_de_ventas["producto3"]=9
print(registro_de_ventas)
#actualizar la cantidad de un producto existente
for producto in registro_de_ventas:
    print("¿Cuanto mas a vendido del",producto,"?")
    registro_de_ventas[producto]= registro_de_ventas[producto] + int(input())
print(registro_de_ventas)
#calcular el total de ventas diarias
total_ventas_diarias= sum(registro_de_ventas.values())
print("El numero total de ventas diarias es:",total_ventas_diarias)


