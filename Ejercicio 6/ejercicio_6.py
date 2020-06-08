def TablaMultiplicar():
    #DATOS DE ENTRADA
    valor=int(input("¿Que numero de la tabla de multiplicar desea resolver?:"))
    valordos=int(input("¿Con que numero desea multiplicarlo?:"))
    #PROCESO Y DATOS DE SALIDA
    contador=1
    while contador<=valordos:
        resultado=valor*contador
        print(f"El resultado de la multiplicacion de {valor}"+"x"+f"{contador}"+" es:"+f" {resultado}")
        contador=contador+1
TablaMultiplicar()
