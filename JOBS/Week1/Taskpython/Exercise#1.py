print("-----Ejercicio #1")

nombre = "Juan"
edad = 10
altura = 1.87

colores = ("Amarillo", "Azul", "Rojo", "Verde")

persona ={
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas ={"manzana", "banano", "pera", "fresa"}

print(f"La altura de juan es {altura}")

if persona["edad"] >= 18:
    print(f"{persona['nombre']}es mayor de edad")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['edad']}es adolecente")
else:
    print(f"{persona['nombre']} es un culicagado por que tiene {edad} años")
    
print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"-{color}")
    
frutas.add("naranja")
print(f"Frutas favoritas: {frutas}")