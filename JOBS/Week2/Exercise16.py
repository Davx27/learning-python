#Cadena Invertida: Pide una palabra al usuario y usa un bucle for para imprimir la palabra al revés.


print("\n       Bienvenido")
palabra = input("Escribe una palabra: ")
invertida = "" 


for letra in palabra:
    invertida = letra + invertida

print("La palabra invertida es:", invertida)
