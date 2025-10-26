#Variable
pets = [
    {"Nombre": "Arenita",    
    "Especie": "Perro",      
    "Edad": 5, 
    "Energia": "Media",     
    "Niños": "si"
    },
      
    {"Nombre": "Esperanza",  
    "Especie": "Gato",       
    "Edad": 6, 
    "Energia": "Media",     
    "Niños": "si"
    },
    
    {"Nombre": "Lupita",     
    "Especie": "Gato",       
    "Edad": 4, 
    "Energia": "Baja",      
    "Niños": "no"
    },
    
    {"Nombre": "Hormiguin",  
    "Especie": "Conejo",     
    "Edad": 2, 
    "Energia": "Baja",      
    "Niños": "si"
    },
    
    {"Nombre": "Juan",       
    "Especie": "Perro",      
    "Edad": 3, 
    "Energia": "Alta",      
    "Niños": "no"
    },
        
    {"Nombre": "Vaco",       
    "Especie": "Conejo",     
    "Edad": 10,
    "Energia": "Alta",      
    "Niños": "no"
    },
       
    {"Nombre": "Lecho",      
    "Especie": "Perro",      
    "Edad": 4, 
    "Energia": "Alta",      
    "Niños": "si"
    },
    
    {"Nombre": "Saturno",    
    "Especie": "Conejo",     
    "Edad": 1, 
    "Energia": "Media",     
    "Niños": "si"
    },
    
    {"Nombre": "Max",        
    "Especie": "Raton",      
    "Edad": 3, 
    "Energia": "Media",     
    "Niños": "si"
    }    
]

preference_user = {}

#fuctions
def filter_pets(preferences):
    compatible = []
    for pet in pets:
        if preferences['Especie'].lower() != "cualquiera":
            if pet['Especie'].lower() != preferences['Especie'].lower():
                continue
                
        if pet['Edad'] < preferences['Edad_minima']:
            continue
        
        if pet['Edad'] > preferences['Edad_maxima']:
            continue
        

        if preferences['Energia'].lower() != "cualquiera":
       
            if pet['Energia'].lower() != preferences['Energia'].lower():
                continue
        
        if preferences['Niños'].lower() != "cualquiera":
            if pet['Niños'].lower() != preferences['Niños'].lower():
                continue
        compatible.append(pet)
    
    if not compatible:
        print("No se encontraron mascotas disponibles... ")
        return
    while True:
        print("Mascotas disponibles")
        for pet in compatible:
            print(f"Nombre: {pet['Nombre']} | Especie: {pet['Especie']} | Edad: {pet['Edad']} | Energia: {pet['Energia']} | Niños: {pet['Niños']}")
    
        pet_user = input("Digite el nombre de la mascota que desea adoptar: ").lower()    
        for pet in compatible:
            if pet['Nombre'].lower() == pet_user:
                print(f"\n{pet}")
                print("\nLa mascota ya es tuya, cuidala mucho :)\n        Que tengas buen dia...")
                pets.remove(pet)
                break
            
            else:
                print("No se encontró esa mascota entre las opciones disponibles.")
                continue
        
        break
def pet_preference():
    species = input("¿Cual especie desea adoptar? (Digite 'cualquiera' si no le importa): ").lower()
    min_age = int(input("¿Edad minima?: "))
    max_age = int(input("¿Edad maxima?: "))
    energia = input("Enrgia, baja, media o alta (Digite 'cualquiera' si no le importa): ").lower()
    kids = input("¿Tiene niños en casa? (Digite 'cualquiera' si no le importa): ").lower()
    
    
    return {
    "Especie": species,
    "Edad_minima": min_age,
    "Edad_maxima": max_age,
    "Energia": energia,
    "Niños": kids
    }
    

        
        

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
                preference_user = pet_preference()
                filter_pets(preference_user)
            case 2:
                for pet in pets:
                    print(f"Nombre: {pet['Nombre']} | Especie: {pet['Especie']} Edad: {pet['Edad']} | Energia: {pet['Energia']} | Niños: {pet['Niños']}")

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
            