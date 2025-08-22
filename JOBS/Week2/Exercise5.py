#Hacer un programa que use una tupla, lista, diccionario, conjunto, para agregar objetos al mismo

tupla = ()

lista = []

diccionario = {}

conjunto = set()

print("\n         Bienvenido al programa de lista de compras para empresarios\n          A continuacioneligiras las cosas q quieres llevarte")
while True:
    print("\n--- Menú ---")
    print("1. Agregar objeto a la lista")
    print("2. Agregar objeto al conjunto")
    print("3. Agregar objeto a la tupla")
    print("4. Agregar objeto al diccionario")
    print("5. Mostrar todas las estructuras")
    print("6. Salir")

    opcion = int(input("\n          Elige una opción: "))

    if opcion == 1:  
        objeto = input("\n          Ingresa un objeto para la lista: ")
        lista.append(objeto)
        print("\n           Objeto agregado a la lista.")

    elif opcion == 2: 
        objeto = input("\n          Ingresa un objeto para el conjunto: ")
        conjunto.add(objeto)
        print("\n           Objeto agregado al conjunto.")

    elif opcion == 3:  # Tupla
        objeto = input("\n          Ingresa un objeto para la tupla: ")
        tupla = tupla + (objeto,)  # creamos una nueva tupla
        print("\n           Objeto agregado a la tupla.")

    elif opcion == 4:  # Diccionario
        clave = input("\n           Ingresa la clave del diccionario: ")
        valor = input("\n           Ingresa el valor para esa clave: ")
        diccionario[clave] = valor
        print("\n           Objeto agregado al diccionario.")

    elif opcion == 5:  
        print("\nLista:", lista)
        print("Conjunto:", diccionario)
        new_var = tupla
        print("Tupla:", new_var)
        print("Diccionario:", diccionario)

    elif opcion == 6:  # Salir
        print("\n           Que le vaya bien my bro\n           No vuelva")
        break

    else:
        print("\n           No puedes hacer eso!!!. Intenta de nuevo... ")
