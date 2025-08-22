#Contador de Vocales: Crea una función que tome una cadena de texto y devuelva el número de vocales que contiene.

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador


cadena = input("Ingresa una frase o palabra: ")
print("La cantidad de vocales es:", contar_vocales(cadena))
