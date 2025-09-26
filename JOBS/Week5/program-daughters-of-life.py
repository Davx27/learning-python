# Variables 
job_offers = []       # Lista para almacenar ofertas laborales
candidates = []       # Lista para almacenar candidatos
profiles = []         # Lista para almacenar perfiles laborales


# Functions 
def register_offer():
    print("\n--- Registrar nueva oferta laboral ---")
    title = input("Título del puesto: ")
    description = input("Descripción del puesto: ")
    salary = float(input("Salario ofrecido: "))

    offer = {
        "Title": title,
        "Description": description,
        "Salary": salary
    }
    job_offers.append(offer)
    print("\n    Oferta registrada con éxito")


def register_candidate():
    print("\n--- Registrar nuevo candidato ---")
    name = input("Nombre del candidato: ")
    age = int(input("Edad: "))
    profession = input("Profesión: ")

    candidate = {
        "Name": name,
        "Age": age,
        "Profession": profession
    }
    
    candidates.append(candidate)
    print("\n Candidato registrado con éxito")


def add_profile():
    print("\n    Agregar perfil laboral ")
    if len(candidates) == 0:
        print(" Primero debe registrar candidatos")
        return
    
    print("\nLista de candidatos:")
    for i, c in enumerate(candidates, 1):
        print(f"{i}. {c['Name']} - {c['Profession']}")

    index = int(input("Seleccione el número del candidato: ")) - 1
    if index < 0 or index >= len(candidates):
        print(" Selección inválida")
        return

    experience = input("Experiencia laboral: ")
    skills = input("Habilidades principales: ")

    profile = {
        "Candidate": candidates[index]["Name"],
        "Experience": experience,
        "Skills": skills
    }
    profiles.append(profile)
    print("\n Perfil laboral agregado con éxito")


menu = True
while menu:
    print("""
    _____________________________________________
    |                                           |
    |        Sistema de Información Laboral     |
    |               ---MENÚ---                  |
    |                                           |
    |-------------------------------------------|
    |  1. Registrar oferta laboral              |
    |  2. Registrar candidato                   |
    |  3. Agregar perfil laboral                |
    |  4. Salir                                 |
    |___________________________________________|
    """)
    
    try:
        option = int(input("Seleccione una opción: "))

        match option:
            case 1:
                register_offer()
            case 2:
                register_candidate()
            case 3:
                add_profile()
            case 4:
                print("\n Hasta pronto...\n")
                menu = False
    except ValueError:
        print("Argumento no valido!!")