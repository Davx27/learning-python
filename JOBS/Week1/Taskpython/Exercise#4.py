print("-----Ejercicio #4")

nombre = "María"
edad = 12
altura = 1.55

colores = ("Amarillo", "Azul Cielo" "Naranja")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"pera", "uvas"}

if persona["edad"] >= 18:
    print(f"{persona['nombre']} es mayor de edad")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} es adolescente")
else:
    print(f"{persona['nombre']} es un niño/a")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("sandía")
print(f"Frutas favoritas: {frutas}")
