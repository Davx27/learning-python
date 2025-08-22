#Menú Interactivo: Crea un menú con opciones (ej. 1. Saludo, 2. Despedida, 3. Salir). Usa un bucle y condicionales
#para ejecutar la acción correspondiente hasta que el usuario elija "Salir".

while True:
    
    print("\n--- Menú ---")
    print("1. Saludo")
    print("2. Despedida")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Adiós! Que tengas un buen día.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break  
    else:
        print("Opción no válida. Intenta de nuevo.")
