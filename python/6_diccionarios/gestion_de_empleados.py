""" Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento. """

informacion_empleados={}
continuar= True

while continuar:
    print("1 -Agregar un empleado.")
    print("2 -Actualizae el salario de un empleado existente.")
    print("3 -Mostrar lista de empleados.")
    print("4 -Calcular el promedio salarial por departamento. ")
    print("5 -Salir")
    opcion = input("Seleccione por numero que opcion desea realizar.")
    #Agregar empleado
    if opcion== "1":
        nombre=input("Ingrese el nombre del nuevo empleado:")
        salario=float(input("Ingrese el salario del nuevo empleado:"))
        departamento=input("Ingrese el nombre del departamento del nuevo empleado:")
        
        informacion_empleados[nombre]={
            "Salario":salario,
            "Departamento":departamento,
        }
    #Actualizar salario de empleado
    elif opcion =="2":
        nombre = input("Ingrese el nombre del empleado que quieres modificarle el salario:")
        if nombre in informacion_empleados:
            nuevo_salario = float(input("Introduzca el nuevo salario:"))
            informacion_empleados[nombre]["salario"]= nuevo_salario
            print("Cambio realizado")
        else:
            print("Ha habido un error o el nombre de usuario no se encuentra")
    #Mostrar lista de empleados
    elif opcion =="3":
        for nombre, informacion in informacion_empleados.items():
            salario = informacion["Salario"]
            departamento = informacion["Departamento"]
            print("--Nombre del empleado:",nombre,"-Salario:",salario,"-Departamento de trabajo:",departamento)
    #Calcular promedio salarial por departamento
    elif opcion == "4":
        departamento = input("Escribe el nombre del departamento del que quieres calcular el promedio salarial:")
        suma_salarios = 0
        contador= 0
        for informacion in informacion_empleados.values():
            if informacion["Departamento"]==departamento:
                suma_salarios= suma_salarios + informacion["Salario"]
                contador = contador + 1
        if contador > 0:
            promedio_salarios= suma_salarios/contador
            print("El promedio salarial del departamento",departamento,"es de",promedio_salarios)
        else:
            print("El deparatamento que buscas no existe")
    #Salir del programa
    elif opcion == "5":
        continuar = False
        print("Hasta la proxima.")
    else:
        print("--La opcion marcada no existe, pruebe con otra.--")
        
        

