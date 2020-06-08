def CantMonedas():
    #DATOS DE ENTRADA
    Mdiez=int(input("Ingrese cuantas monedas de diez pesos tiene:"))
    Mcinco=int(input("Ingrese cuantas monedas de cinco pesos tiene:"))
    Mpeso=int(input("Ingrese cuantas monedas de un peso tiene:"))
    Bdiez=int(input("Ingrese cuantos billetes de diez pesos tiene:"))
    Bveinte=int(input("Ingrese cuantos billetes de veinte pesos tiene:"))
    Bcincuenta=int(input("Ingrese cuantos billetes de cincuenta pesos tiene:"))
    #PROCESO
    cantidad1=Mdiez*0.10
    cantidad2=Mcinco*0.50
    cantidad3=Mpeso*1
    cantidad4=Bdiez*10
    cantidad5=Bveinte*20
    cantidad6=Bcincuenta*50
    total=cantidad1+cantidad2+cantidad3+cantidad4+cantidad5+cantidad6
    #DATOS DE SALIDA
    print(f"Usted tiene: {total}"+" Pesos"+" en su monedero")
CantMonedas()