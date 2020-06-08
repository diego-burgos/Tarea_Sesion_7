def SueldoSemanal():
    #DATOS DE ENTRADA
    sueldoH=int(input("Ingrese el sueldo por hora: "))
    #PROCESO Y DATOS DE SALIDA
    while True:
        nombre=input("Ingrese el nombre del trabajador: ")
        horas=int(input("Ingrese las horas trabajadas por dia: "))
        sueldoD=horas*sueldoH
        sueldo=sueldoD*7
        if sueldo<=150:
            sueldoP=sueldo+(sueldo*0.5)
            sueldoF=sueldoP-sueldo
        elif sueldo<=300:
            sueldoP=sueldo+(sueldo*0.7)
            sueldoF=sueldoP-sueldo
        elif sueldo<=450:
            sueldoP=sueldo+(sueldo*0.9)
            sueldoF=sueldoP-sueldo
        print(f"El sueldo semanal del trabajor: {nombre}"+f" es de: {sueldoF}"+" Pesos")
        x=input("Desea continuar? SI/NO: ")
        if x!="SI":
            break
SueldoSemanal()