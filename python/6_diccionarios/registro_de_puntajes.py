""" Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores. """

score={}
#ingresar nombres y puntajes
continuar=True

while continuar:
    nombre= input("Escriba el nombre del jugador (o /salir/ para continuar: ")
    if nombre.lower() == "salir":
        continuar=False
    else:
        puntaje=int(input("Escriba el puntaje obtenido:"))
        score[nombre]=puntaje

#obtener puntaje mas alto
        puntaje_mas_alto=(max(score.values()))
        nombre_jugador = (max(score, key=score.get))
        print("El puntaje mas alto es:")
        print(nombre_jugador,":", puntaje_mas_alto,"puntos.")
#promedio de puntajes
        promedio_puntajes= sum(score.values())/len(score.values())
        print("El promedio de puntajes es:",promedio_puntajes)
#cantidad total de jugadores
cantidad_total_jugadores= len(score)
print("La cantidad total de  jugadores es de:",cantidad_total_jugadores)
    
