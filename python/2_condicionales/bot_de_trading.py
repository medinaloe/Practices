"""Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
estrictamente por encima de 150 el bot deberá imprimir la orden de vender"""

precio_usuario = float (input("Introduzca la cantidad de dinero que quiera: "))

if precio_usuario < 100 :
    print ("Ordenar compra.")
elif (precio_usuario >= 100) and (precio_usuario < 150):
    print ("Activar orden Hold.")
elif precio_usuario >= 150 :
    print ("Activar venta.")