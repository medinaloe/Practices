"""En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
con esas piezas."""

pieza1 = float (input ("Escribe la longitud de la primera pieza: "))
pieza2 = float (input ("Escribe la longitud de la segunda pieza: "))
pieza3 = float (input ("Escribe la longitud de la tercera pieza: "))

if (pieza1 + pieza2 > pieza3) and (pieza1 + pieza3 > pieza2) and (pieza2 + pieza3 > pieza1):
    print ("Si se podria construir un triangulo con esas piezas.")
else :
    print ("No se ouede construir el triangulo con las piezas que tenemos.")