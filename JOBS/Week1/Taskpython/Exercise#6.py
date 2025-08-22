print("-----Ejercicio #6")

nombre = "Laura"
edad = 14
altura = 1.62

colores = ("Rosa", "Morado", "Lila")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"frambuesa", "arándano"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es un niño/a")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} está en edad escolar")
else:
    print(f"{persona['nombre']} es adulto")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("manzana")
print(f"Frutas favoritas: {frutas}")
