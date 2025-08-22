print("-----Ejercicio #8")

nombre = "Sofía"
edad = 11
altura = 1.48

colores = ("Morado", "Azul Bebe ","Celeste")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"pera", "manzana"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es una niña cansona")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} está en la adolescencia")
else:
    print(f"{persona['nombre']} es adulta")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("cereza")
print(f"Frutas favoritas: {frutas}")
