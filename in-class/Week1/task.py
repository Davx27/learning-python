print("-----Ejercicio #1")

nombre = "Juan"
edad = 10
altura = 1.87

colores = ("Amarillo", "Azul", "Rojo", "Verde")

persona ={
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas ={"manzana", "banano", "pera", "fresa"}

print(f"La altura de juan es {altura}")

if persona["edad"] >= 18:
    print(f"{persona['nombre']}es mayor de edad")
elif 13 <= persona["edad"] <= 17:
    print(f"{persona['edad']}es adolecente")
else:
    print(f"{persona['nombre']} es un culicagado por que tiene {edad} años")
    
print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"-{color}")
    
frutas.add("naranja")
print(f"Frutas favoritas: {frutas}")

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

print("\n-----Ejercicio #3")

nombre = "Luis"
edad = 15
altura = 1.75

colores = ("Negro", "Gris")

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

print("\n-----Ejercicio #4")

nombre = "María"
edad = 12
altura = 1.55

colores = ("Amarillo", "Naranja")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"pera", "uvas"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es un niño/a")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("sandía")
print(f"Frutas favoritas: {frutas}")

print("\n-----Ejercicio #5")

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

if persona["edad"] >= 18:
    print(f"{persona['nombre']} puede votar")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("naranja")
print(f"Frutas favoritas: {frutas}")

print("\n-----Ejercicio #6")

nombre = "Laura"
edad = 14
altura = 1.62

colores = ("Rosa", "Lila")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"frambuesa", "arándano"}

if 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} está en edad de ir al colegio")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("manzana")
print(f"Frutas favoritas: {frutas}")

print("\n-----Ejercicio #7")

nombre = "Miguel"
edad = 25
altura = 1.90

colores = ("Negro", "Purpura", "Blanco")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"sandía", "piña"}

if persona["edad"] >= 18:
    print(f"{persona['nombre']} es adulto joven")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("coco")
print(f"Frutas favoritas: {frutas}")

print("\n-----Ejercicio #8")

nombre = "Sofía"
edad = 11
altura = 1.48

colores = ("Morado","Azul", "Celeste")

persona = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "coloresFavoritos": colores
}

frutas = {"pera", "bananno", "manzana"}

if persona["edad"] < 13:
    print(f"{persona['nombre']} es un niño/a feliz")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("cereza")
print(f"Frutas favoritas: {frutas}")

print("\n-----Ejercicio #9")

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

if 13 <= persona["edad"] <= 17:
    print(f"{persona['nombre']} es un adolescente responsable")

print(f"Colores favoritos de {persona['nombre']}:")
for color in persona["coloresFavoritos"]:
    print(f"- {color}")

frutas.add("piña")
print(f"Frutas favoritas: {frutas}")

