def NumerosNaturales():
    #DATOS DE ENTRADA
    cantN=int(input("Ingrese la cantidad de numeros a resolver:"))
    #PROCESO Y DATOS DE SALIDA
    contador=1
    while contador<=cantN:
        valor=int(input(f"Ingrese el numero {contador}: "))
        cubo=valor**3
        print(f"El cubo de el valor es:"+f" {cubo}")
        contador=contador+1
NumerosNaturales()
