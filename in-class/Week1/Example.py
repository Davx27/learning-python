# Variables y tipos
nombre = "David"
edad = 17
altura = 1.65

# Tupla (colores favoritos, no cambian)
colores = ("rojo", "verde", "azul")

# Diccionario
persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "colores_favoritos": colores  # guardamos la tupla aquí
}

# Conjunto (frutas favoritas, elementos únicos)
frutas = {"manzana", "pera", "uva"}

# Condicional
if persona["edad"] >= 18:
    print(f"{persona['nombre']} es mayor de edad.")
elif persona["edad"] >= 13:
    print(f"{persona['nombre']} es adolescente.")
else:
    print(f"{persona['nombre']} es menor de edad.")

# Mostrar colores favoritos usando la tupla dentro del diccionario
print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["colores_favoritos"]:
    print(f"- {color}")

# Agregar una fruta nueva al conjunto y mostrarlo
frutas.add("naranja")
print(f"Frutas favoritas: {frutas}")
