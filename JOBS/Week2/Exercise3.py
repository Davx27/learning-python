#Hcaer un programa que construya una contraseña aleatoria con caracteres diferentes de maximo 8
continuar = True
while continuar:
    print("""Bienvenio
Crea tu contraseña segura facil y rapido
""")
    import random

    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    tope = True
    
    
    
    
    
    
    
    
    
    
    while tope:
        longitud = int(input("¿De cuantos caracteres quieres tu contraseña? Maximo 8 caracteres: "))
        if longitud < 8:
        
            print("Correcto")
            tope = False 
        else:
            print("MAXIMO 8 CARACTERES, intente de nuevo... ")
            
            
        
    contraseña = "".join(random.sample(caracteres, longitud))

    print("Tu contaseña es : ", contraseña)
    respuesta = input("¿Desea crear otra contraseña aleatoria? (SI/NO): ").lower()
    if respuesta != "si":
        continuar = False
        print("""
Gracias por usar nuestro programa
Buena suerte... """)
        
