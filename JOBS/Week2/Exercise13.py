#Números Primos: Pide un número al usuario y usa un bucle para determinar si es un número primo.
numero = int(input("Ingresa un número: "))


if numero < 2:
    print(numero, "no es un número primo.")
else:
    es_primo = True  
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False  
            break  
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
