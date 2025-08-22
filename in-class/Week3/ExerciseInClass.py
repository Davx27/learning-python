#Apartado de funciones
def mediaDeNotas(notas):
    return sum(notas) /len(notas)


#Variables de menu
play = True  


while play:
    
    print("""
    _________________________________________________
    |                                               |
    |       BIENVENIDO A TU MENU INTERACTIVO        |
    |                                               |
    |   1.Programa de suma                          |
    |   2.Programa de nota                          |
    |   3.Programa de retiro de cajero automatico   |
    |   4.Gestor de tareas                          |
    |   5.Salir del menu                            |
    |                                               |
    |_______________________________________________|   
    """)

    option = int(input("\n          Seleccione una opcion...\n"))
    
    
    #option 1 programa de sumas
    
    if option == 1: 

        print("\n           PROGRAMA DE SUMA\n")
        print("\n           A continucaion ingresa dos valores para sumar\n")
        num1  = float(input("\n           Primer valor: \n"))
        num2  = float(input("\n           Segundo valor: \n"))
        result1 = num1 + num2 
        print("Tu resultado es: ", result1)
        
        action1 = (input("\n           ¿Deseas hacer otra suma? (SI/NO): ")).lower()
        if action1 != "si":
            print("\n           Volviendo al menu...\n")                
            
            
        elif action1 == "si":
            print("\n           OK\n")
            
        else:
            print("\n           ¡¡¡Intente de nuevo!!!")
            
            
    #opcion 2 programa de promedio de notas  
            
    elif option == 2:
        
        print("\n           PROGRAMA DE NOTA\n")
        notas = []
        while True:         #Bucle para definir las notas a promediar del usuario
            noteLength = (int(input("¿Cuantas notas deseas promediar?: ")))
            
            if 1 < noteLength <= 25:
                break
            else:
                print("\n           Ingrese un valor entre 2 y 25 ")
            
        for i in range (noteLength):            #Bucle para definir el promedio de las notas del usuario
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)
            
        result2 = mediaDeNotas(notas)
        print(f"\n           Tu resultado es {result2}: ")
        
        accion2 = (input("\n             ¿Deseas promedias mas notas? (SI/NO):")).lower()
        if accion2 != "si":
            print("\n           Volviendo al menu...\n")
        
        else:
            print("\n           ¡¡¡Intente de nuevo!!!")
            
            
    elif option == 3:
        print("\n           PROGRAMA DE RETIRO DE CAJERO AUTOMATICO\n ")
        
        
    elif option == 5:
        print("\n           Vuelva pronto...\n")
        play = False

        


