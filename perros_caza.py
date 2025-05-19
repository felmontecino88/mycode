# import random

# cuota_min=random.randint(2,5)
# cumple=0
# no_cumple=0
# while True:
#     try:
#         cant=int(input("¿Cuantos perros de caza son?"))
#     except Exception:
#         print("Solo se aceptan numeros enteros")

# print("La cuota mínima de conejos es", cuota_min)

# for i in range(cant):
#     op=random.randint(2,8)
#     print("El perro", i+1, "trajo", op, "conejos")
#     if op > cuota_min:
#         print("Gana filete")
#         cumple+=1
#     else:
#         print("No gana filete")
#         no_cumple+=1

# print(cumple, "perros cumplieron")
# print(no_cumple, "perros no cumplieron")

cant=int(input("¿Cuantos perros de caza son?"))