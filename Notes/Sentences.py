# Break: permite salir de un bucle cuando se cumple una condicion

for numero in range(1, 6):
    if numero == 5:
        break # Deascanso o interrupcion en este punto.
    print(numero)
    
print("Bucle terminado")

# Continue omite una parte del bucle cuando se cumple una condicion y continua con el resto

for numero in range(1, 6):
    if numero == 5:
        continue # Salta las iteraciones siguientes y sigue con siguiente item
    print(numero) # Lo que sucede en este caso: no se ejecuta 'print(numero)' debido que desde el continue salta al siguiente item
                  
print("Bucle terminado")

# Pass: Permite continuar con una sentenciao funcion que ya no tiene o aun no tiene un bloque de codigo util

for numero in range(1, 6):
    if numero <= 3:
        #Aqui no pasa nada y el bicle sigue trabajando
        pass 
    else: 
        print("El siguiente valor es mayor a 3:")
    print(numero)
    
print("Bucle terminado")
