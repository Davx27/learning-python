print("\n-----Ejercicio #2")

nombre = "Ana"
edad = 22
altura = 1.60

colores = ("Rosa", "Blanco", "Morado")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"fresa", "melón", "kiwi"}

if persona["edad"] >= 18:
    print(f"{persona['nombre']} es mayor de edad")
else:
    print(f"{persona['nombre']} es menor de edad")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("cereza")
print(f"Frutas favoritas: {frutas}")