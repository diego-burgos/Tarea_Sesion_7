def AhorroDiario():
    #DATOS DE ENTRADA
    diario=int(input("Ingrese cuanto ahorro el primero de enero:"))
    #PROCESO Y DATOS DE SALIDA
    dia=1
    while dia<=365:
        print(f"Ahorro dia {dia} es:"+f"{diario}"" pesos")
        diario=diario*3
        dia=dia+1
AhorroDiario()