import random
import time
total_alum=int(input("¿Cuantos alumnos son?"))

azul=0
rojo=0

# for t in range(total_alum):
#         nota=random.randint(1,7)
#         print("El alumno", t+1, "obtuvo", nota)
#         if nota >= 4:
#             azul+=1
#         else:
#             rojo+=1

# print("La cantidad de rojos es", rojo)
# time.sleep(1)

for i in range(total_alum):
    nota=random.randint(1,7)
    print("El alumno", i+1, "obtuvo", nota)
    if nota >= 4:
        azul+=1
    else:
        rojo+=1
        decimas=0
        print("El alumno", i+1, "asistió al taller 1? (s/n)")
        talleres=str(input())
        if talleres == "s":
            decimas+=1
        print("El alumno", i+1, "asistió al taller 2? (s/n)")
        talleres=str(input())
        if talleres == "s":
            decimas+=1
        print("El alumno", i+1, "asistió al taller 3? (s/n)")
        talleres=str(input())
        if talleres == "s":
            decimas+=1
        print("El alumno", i+1, "asistió al taller 4? (s/n)")
        talleres=str(input())
        if talleres == "s":
            decimas+=1
    decimas_total=decimas*0.3
    if decimas_total > 1:
        print("Obtuvo la bendición del profe")
    else:
        print("No se le puede ayudar")
    print("La nota final del alumno", i+1, "es", nota+decimas_total)

