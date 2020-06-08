def IncrementodeSalario():
    #DATOS DE ENTRADA
    salario=int(input("Ingrese su salario inicial:"))
    años=int(input("Ingrese los años que desea calcaular:"))
    #PROCESO Y DATOS DE SALIDA
    x=1
    while x<=años:
        salario=salario+(salario*0.10)
        print(f"El salario en el año: {x}"+f" es de: {salario}"+" $")
        x=x+1
IncrementodeSalario()        