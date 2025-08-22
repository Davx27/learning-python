#Hacer un programa que imprima las tablas de multiplicar desde el 2 al 9

continuar = True
while continuar:
    number = int(input(""" 
Bienvenido a nuestro programa de las tablas de multiplicar

A continucion ingresa un numero de la tabla
de multiplicar que deseas ver (2 al 9): """))

    for i in range(2, 10):
        resultado = i * number
        print(number, " x ", i, " = ", resultado)

    respuesta = input("¿Desea ver otra tabla? (Si/No): ").lower()
    if respuesta != "si":
        continuar = False
        print("Hasta la proxima")