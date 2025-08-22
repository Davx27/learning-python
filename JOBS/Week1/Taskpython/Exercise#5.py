print("-----Ejercicio #5")

nombre = "Carlos"
edad = 18
altura = 1.80

colores = ("Azul", "Verde", "Blanco")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"kiwi", "melon", "durazno"}

if persona["edad"] > 18:
    print(f"{persona['nombre']} es adulto")
elif persona["edad"] == 18:
    print(f"{persona['nombre']} acaba de cumplir la mayoría de edad")
else:
    print(f"{persona['nombre']} es menor de edad")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("naranja")
print(f"Frutas favoritas: {frutas}")
