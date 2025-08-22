#Factorial de un Número: Escribe una función que calcule el factorial de un número dado.
def factorial(n):
    if n < 0:
        return "El factorial no está para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número para calcular su factorial: "))
print("El factorial de", numero, "es:", factorial(numero))
