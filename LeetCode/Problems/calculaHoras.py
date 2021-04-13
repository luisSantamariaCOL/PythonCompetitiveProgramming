hora_levantarse = int(input("¿A qué hora te levantaste? (0/23)\n"))
print("Te levantaste a las", hora_levantarse)

hora_acostarse = int(input("¿A qué hora te acostarás? (0/23)\n"))
print("Te acostarás a las", hora_acostarse)
if hora_acostarse > hora_levantarse:
    print("Despierto", (hora_acostarse-hora_levantarse), "horas")

else:
    print("Despierto", (24-hora_levantarse)+hora_acostarse, "horas")

tiempo_estudio = int(input("¿Cuántas horas vas a estudiar (0/12)\n"))
horas = [x for x in range(24)]
horas.extend([x for x in range(10)])
tiempo_trabajo = 2
estudio = False
tiempo_actual = hora_levantarse
while tiempo_estudio > 0:

    if  not estudio:
        print("descanso", horas[tiempo_actual], "-", horas[tiempo_actual+1])
        tiempo_actual = tiempo_actual + 1
        estudio = True
    if estudio:
        print("estudio", horas[tiempo_actual], "-", horas[tiempo_actual+2])
        tiempo_estudio = tiempo_estudio-2
        tiempo_actual = tiempo_actual + 2
        estudio = False


