"""En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
ingredientes."""

pedido = int (input ("Buenas que tipo de hamburguesa desea tomar: 1-hamburguesa clasica / 2-hamburguesa vegana.(Marque los numeros) "))
ingredientes_clasica ="bacon", "huevo", "Queso Idiazabal" 

if pedido == 1 :
    ingredientes_clasica = int (input ("Genial, los ingredientes extra de la hamburguesa clasica son los siguientes, elige los que quiera: 1-bacon, 2-huevo y 3-Queso Idiazabal(marque los numeros) ")) 
    print (ingredientes_clasica)
else:
 print ("Genial, los ingredientes extra de la hamburguesa vegana son los siguientes, elige los que quiera: tofu, cebolla caramelizada ")