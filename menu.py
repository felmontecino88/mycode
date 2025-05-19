# lavado de autos
# crear un menu para lavar autos
# 1.- ingresar vehiculo (obviar, no se puede)
# 2.- cursar pago del lavado
# 3.- ver ventas diarias
# 4.- salir
# el lavado tiene 3 niveles
# 1.- full $15000, 2.- standard $10000, 3.- basico $7000
# al mostrar las ventas diarias, debe mostrar la cantidad de autos que han ingresado y el monto total racaudado
# tambien debe mostrar el monto total pagado

full=0
standard=0
basico=0

while True:
    print("""¡Bienvenido al lavado de autos!
          1.- Cursar pago del lavado
          2.- Ver ventas diarias
          3.- Salir""")
    op=int(input())
    while op==1:
            print("""Elija tipo de lavado:
                1.- Full (15000)
                2.- Standard (10000)
                3.- Basico ($7000)
                4.- Volver""")
            op_1=int(input())
            if op_1 == 1:
                full+=1
            elif op_1 == 2:
                standard+=1
            elif op_1 == 3:
                basico+=1
            elif op_1 == 4:
                break
    while op==2:
            print(f"""Las ventas diarias son:
                Full: {full}
                Standard: {standard}
                Basico: {basico}
                Total autos: {full+standard+basico}
                Total ingresos: {(full*15000)+(standard*10000)+(basico*7000)}""")
            volver=input("Presione cualquier tecla para volver")
            break
    while op==3:
         break
    print("Gracias por usarme")

