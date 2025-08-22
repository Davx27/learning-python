print("-----Ejercicio #7")

nombre = "Miguel"
edad = 25
altura = 1.90

colores = ("Negro", "Gris", "Blanco")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"sandía", "piña"}

if persona["edad"] < 18:
    print(f"{persona['nombre']} es menor de edad")
elif 18 <= persona["edad"] <= 30:
    print(f"{persona['nombre']} es un adulto joven")
else:
    print(f"{persona['nombre']} es adulto mayor")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("coco")
print(f"Frutas favoritas: {frutas}")
