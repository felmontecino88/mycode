'''Crear un menu de carrito con las siguientes opciones
1.-Ingresar nombre del usuario
Sera mostrado en la boleta, con un saludo
2.- Comprar, poner productos para poder comprar con su precio correspondiente
3.- Sacar boleta, calcular el precio neto y el precio más IVA. Mostrar totales
4.- Salir

Consideraciones:
Por lo menos 3 productos
No hay limite de compra
Se puede salir en caulquier moemnto
Los montos de los productos son fijos'''

total=0
nom="user"

while True:
    op=int(input('''Elija una opción:
                 1.- Ingresar nombre
                 2.- Comprar productos
                 3.- Ver boleta
                 4.- Salir'''))
    match op:
        case 1:
            print("Ingrese su nombre")
            nom=str(input())
            print("Bienvenido", nom)
        case 2:
            total=0
            while True:
                print('''Elija sus productos:
                    1.- Leche 1Lt ($1200)
                    2.- Carne 1Kg ($8000)
                    3.- Pan de molde ($2000)
                    4.- Salir''')
                prod=int(input())
                if prod==4:
                    break
                print("¿Cuantas unidades desea?")
                uni=int(input())
                if prod==1:
                    total=total+1200*uni
                elif prod==2:
                    total=total+8000*uni
                elif prod==3:
                    total=total+2000*uni
                print(total)
        case 3:
            print("el total de su compra es", total)
            print("el total más IVA es", total*1.19)
        case 4:
            break
        case _:
            print("Opción inválida")

print("Gracias por usarme", nom)