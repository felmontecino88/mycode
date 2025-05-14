import random

def gen_tab():
    numero=int(input("Elija un numero"))
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero} x {i} = {resultado}")

def num_sec():
    secreto = random.randint(1, 100)
    intentos = 5

    print("¡Bienvenido al juego del número secreto!")
    print("Adivina un número entre 1 y 100. Tienes 5 intentos.")

    for intento in range(1, intentos + 1):
        try:
            numero = int(input(f"Intento {intento}: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero == secreto:
            print(f"¡Felicidades! Adivinaste el número en {intento} intento(s).")
            break
        elif numero < secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
    else:
        print(f"Lo siento, se acabaron los intentos. El número era {secreto}.")

def all():
    menu=int(input("""Elije una opción:
                1.- Numero secreto
                2.- Generador de tablas
                3.- Salir"""))
    while menu!=3:
        match menu:
            case 1:
                num_sec()
                choice=str(input("¿Desea continuar? s/n"))
                choice=choice.lower()
                if choice == "s":
                    num_sec()
                elif choice == "n":
                    all()
            case 2:
                gen_tab()
                choice=str(input("¿Desea continuar? s/n"))
                choice=choice.lower()
                if choice == "s":
                    gen_tab()
                elif choice == "n":
                    all()
            case 3:
                break

menu=int(input("""Elije una opción:
               1.- Numero secreto
               2.- Generador de tablas
               3.- Salir"""))
while menu!=3:
    match menu:
        case 1:
            num_sec()
            choice=str(input("¿Desea continuar? s/n"))
            choice=choice.lower()
            if choice == "s":
                num_sec()
            elif choice == "n":
                all()
        case 2:
            gen_tab()
            choice=str(input("¿Desea continuar? s/n"))
            choice=choice.lower()
            if choice == "s":
                gen_tab()
            elif choice == "n":
                all()
        case 3:
            break

print("¡Gracias por usarme!")