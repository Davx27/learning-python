print("-----Ejercicio #10")

nombre = "Valentina"
edad = 19
altura = 1.65

colores = ("Rojo", "Negro", "Blanco")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"manzana", "pera", "fresa"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es un niño/a")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} está en la adolescencia")
else:
    print(f"{persona['nombre']} es mayor de edad")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("mango")
print(f"Frutas favoritas: {frutas}")
