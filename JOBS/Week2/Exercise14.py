#Adivina el Número: Genera un número aleatorio del 1 al 10. Usa un bucle while para pedir al usuario que adivine el número. Muestra si su intento fue muy alto o muy bajo. El bucle termina cuando adivina correctamente.

import random  

numero_secreto = random.randint(1, 10)
print()
print("         ¡Adivina el número bro! Está entre 1 y 10.")

while True:
    intento = int(input("\n             Ingresa tu intento: "))

    if intento < numero_secreto:
        print("         Un poco mas bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("         Un poco mas alto. Intenta otra vez.")
    else:
        print("         Adivinaste el número bro:", numero_secreto)
        break