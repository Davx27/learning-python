#hacer un programa que halle el promedio de 10 notas

def MediaDeNotas(notas):
    return sum(notas) / len(notas)

notas = []

print("""
Bienvenido a tu programa de promedio de notas

Danos tus 10 notas a continiacion...

(Recuerde que este sistema esta diseñado para promediar notas de 0 a 5)

""")

for i in range (10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
    
promedio = MediaDeNotas(notas)
print(f"""
Tu promedio de notas es: {promedio}""")

if promedio >= 40:
    print("Eres alguien muy jucios@")
elif 33 <= promedio <= 39:
    print("Pasaste raspando, tienes que ponerte juicios@")
else:
    print("Dedicate a vender bonice, te va ir mejor")

print("""Gracias por usar nuestro programa
Vuelva pronto...""")



 