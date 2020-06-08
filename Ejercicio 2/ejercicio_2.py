def PagodeHamburguesa():
    #DATOS DE ENTRADA
    sencillas=int(input("¿Cuantas hamburguesas de tipo sencilla desea?:"))
    dobles=int(input("¿Cuantas hamburguesas de tipo doble desea?:"))
    triples=int(input("¿Cuantas hamburguesas de tipo triple desea?:"))
    #PROCESO Y DATOS DE SALIDA
    pagoS=sencillas*20
    pagoD=dobles*25
    pagoT=triples*28
    pago=pagoS+pagoD+pagoT
    tipoP=input("¿Desea pagar con tarjeta de credito?:")
    if tipoP=="SI":
        pagoF=pago+(pago*0.5)
        print("El monto a pagar es de: "+f"$ {pagoF}")
    else:
        pagoF=pago
        print("El monto a pagar es de: "+f"$ {pagoF}")
PagodeHamburguesa()