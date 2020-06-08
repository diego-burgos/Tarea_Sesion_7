def NotaNAlumnos():
    #DATOS DE ENTRADA
    NAlumnos=int(input("Ingrese la cantidad de alumnos:"))
    #PROCESO 
    contador=1
    aprobados=0
    reprobados=0
    i=1
    for i in range(NAlumnos):
        nota=int(input(f"Ingrese la nota del alumno {contador}:"))
        contador=contador+1
        i=i+1
        if nota<=12:
            reprobados=reprobados+1
        elif nota>=13:
            aprobados=aprobados+1
    #DATOS DE SALIDA
    print(f"Los alumnos que aprobaron son: {aprobados}")
    print(f"Los alumnos que reprobaron son: {reprobados}")
NotaNAlumnos()



