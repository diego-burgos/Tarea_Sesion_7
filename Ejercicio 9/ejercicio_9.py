def CuentadeAhorros():
    #DATOS DE ENTRADA
    inversionI=int(input("Ingrese el monto que ingreso en su cuenta de ahorros:"))
    añoP=int(input("¿En que año deposito el dinero?:   "))
    añoA=int(input("Ingrese el año actual:   "))
    #PROCESO
    año=añoA-añoP
    porcentaje=año*0.15
    ganancia=inversionI+(inversionI*porcentaje)
    #DATOS DE SALIDA
    print("Su inversion hasta ahora tiene un valor de:"+" $ "+f" {ganancia}")
CuentadeAhorros()