print("\n-----Ejercicio #3")

nombre = "Luis"
edad = 15
altura = 1.75

colores = ("Negro", "Platead", "Gris")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"manzana", "pera", "mango"}

if 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} es adolescente")
else:
    print(f"{persona['nombre']} no es adolescente")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("banana")
print(f"Frutas favoritas: {frutas}")
