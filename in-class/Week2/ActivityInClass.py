#Hcer un programa que imprima las tablas de multiplicar desde el 2 al 9

numero = int(input("""Bienvenido a nuestro programa de multiplicar
A continucion ingresa un numero de la tabla de multiplicar que deseas ver (2 al 9): """))
for tabla in range(2, 10):
    print (f"Esta es la tabla del {tabla}")

    for i in range(1, 10):
        resultado = tabla * i
        print(numero, "x", i, "=", resultado)

continuar = input("¿Deseas ver otra tabla? (Si/No): ").lower() == 'si'
if continuar != 'si':
    print("Hasta la proxima")

    
    
    

