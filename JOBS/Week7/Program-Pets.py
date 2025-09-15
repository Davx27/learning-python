#Variable
pets = [
    {"Nombre": "Arenita",    "Especie": "Perro",      "Edad": 5, "Energia": "Media",     "Compatible con niños": "SI"},  
    {"Nombre": "Esperanza",  "Especie": "Gato",       "Edad": 6, "Energia": "Media",     "Compatible con niños": "SI"},
    {"Nombre": "Lupita",     "Especie": "Gato",       "Edad": 4, "Energia": "Baja",      "Compatible con niños": "NO"},
    {"Nombre": "Hormiguin",  "Especie": "Conejo",     "Edad": 2, "Energia": "Baja",      "Compatible con niños": "SI"},
    {"Nombre": "Juan",       "Especie": "Perro",      "Edad": 3, "Energia": "Alta",      "Compatible con niños": "NO"},    
    {"Nombre": "Vaco",       "Especie": "Conejo",     "Edad": 10,"Energia": "Alta",      "Compatible con niños": "NO"},   
    {"Nombre": "Lecho",      "Especie": "Perro",      "Edad": 4, "Energia": "Alta",      "Compatible con niños": "SI"},
    {"Nombre": "Saturno",    "Especie": "Conejo",     "Edad": 1, "Energia": "Media",     "Compatible con niños": "SI"},
    {"Nombre": "Max",        "Especie": "Raton",      "Edad": 3, "Energia": "Media",     "Compatible con niños": "SI"}    
]

#fuctions


menu = True
while menu:
    print("""
                _____________________________________________
                |                                           |
                |             Adopt Pet Program             |
                |             ---BIENVENIDOS---             |
                |                                           |
                |-------------------------------------------|
                |                                           |
                |  1.Adopte Aqui                            |
                |  2.Ver las mascotas sin adoptar           |
                |  3.Salir del sistema                      |
                |                                           |
                |___________________________________________|
                """)
    try:
        option = int(input("\n         Seleccione una opcion: "))
        match option:
            case 1:
                None
            case 2:
                None
            case 3:
                print(""" 
                    ______________________________________________
                    |                                            |
                    |           Que Tenga un Feliz Dia           |
                    |                                            |
                    |           Vuelva Pronto!!!                 |
                    |                                            |
                    |____________________________________________|""")
                menu = False
    except ValueError:
        print("Argumento no valido!!!")
            