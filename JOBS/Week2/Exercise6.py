#Par o Impar: Pide un número al usuario y usa un condicional para determinar si es par o impar.

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")