print("-----Ejercicio #9")

nombre = "Andrés"
edad = 17
altura = 1.70

colores = ("Azul", "Negro")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"melón", "mango"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es un niño")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} es un adolescente responsable")
else:
    print(f"{persona['nombre']} es adulto")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("piña")
print(f"Frutas favoritas: {frutas}")
