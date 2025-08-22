#Hacer un programa que simule un motor de un carro en movimiento con 4 velocidades

encendido = False
marcha = 1
velocidad = 0
print("\n--- Simulación del motor ---")

while True:
    encendido = int(input("\n           1.Encender motor: \n           2.Salir del auto: \n           :"))
    if encendido == 1:
        print("         Encendiendo auto")
    elif encendido == 2:
        break
        
    
    while True:
        print("1. Acelerar")
        print("2. Desacelerar")
        print("3. Subir marcha")
        print("4. Bajar marcha")
        print("5. Apagar motor")
    
        accion = int(input("Elige una opción: "))
        match accion:
            case 1:
                limite = marcha * 40
                if velocidad < limite:
                    velocidad += 10
                    print("\n          El carro ahora va a, ", velocidad, "km/h (Marcha", marcha, ")")
                else:
                    print("\n           Ya estas al limite de la marcha ", marcha, "\n           A ",marcha * 40, "km/h")

            case 2:
                if velocidad > 0:
                    velocidad -= 10
                    print("\n          Estas desacelerando... ")
                    print("\n          El carro ahora va a, ", velocidad, "km/h (Marcha", marcha, ")")
                else: 
                    print("\n           Ya frenaste, calmate...")

            case 3:  # Multiple values
                if marcha < 4:
                    marcha += 1
                    print("\n            Subiste de marcha", marcha, "\n")    
                else:
                    print("\n            Ya estas en la maxima marcha", marcha, "\n")

            case 4:  # Default case
                if marcha > 1:
                    marcha -= 1
                    print("\n            Bajase de marcha", marcha, "\n")
                else:
                    print("\n            Ya estas en la minima marcha", marcha, "\n")

            
            case 5:  # Default case
                encendido = False
                velocidad = 0
                marcha = 1
                print("\n            Apagando y saliendo del auto\n")
                break

print("Vuelva pronto\nMi dios me lo bendiga")
