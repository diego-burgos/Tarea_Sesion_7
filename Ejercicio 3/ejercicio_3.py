def nCantidad():
    #DATOS DE ENTRADA
    Ncantidad=int(input("Ingrese la cantidad de numeros que desea leer:"))
    #PROCESO Y DATOS DE SALIDA
    cero=0
    menorescero=0
    mayorescero=0
    contador=1
    while contador<=Ncantidad:
        numero=int(input(f"Ingrese el valor de la posicion {contador} :"))
        if numero<0:
            menorescero=menorescero+1
        elif numero==0:
            cero=cero+1
        else:
            mayorescero=mayorescero+1
        contador=contador+1
    print(f"La cantidad de numeros menores a 0 es: {menorescero}")
    print(f"La cantidad de numeros iguales a 0 es: {cero}")
    print(f"La cantidad de numeros mayores a 0 es: {mayorescero}")
nCantidad()