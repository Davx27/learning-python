#Función Suma: Crea una función llamada sumar_dos_numeros que tome dos argumentos y devuelva su suma. Muestra el resultado.

def sumar_dos_numeros(a, b):
    return a + b  

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

resultado = sumar_dos_numeros(num1, num2)

print("La suma de", num1, "y", num2, "es:", resultado)
