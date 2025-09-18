# Variable

staff = [
    {"Nombre": "Alejo",
     "Desempeño semanal": [9, 7.5, 9],
     "Estado": "Sobresaliente",
     "Promedio": 8.5
     }
]

# Fuctions section

def average_performance(data):
    return sum(data) / len(data) if data else 0

def register_data_staff():
    name = input("Nombre del empleado: ").title()
    weeks = []
    state = []
    for i in range(3):
        note = float(input(f"Desempeño laboral semana {i+1} : "))
        weeks.append(note)
    
        
    average = average_performance(weeks)
    if average >= 8.5:
        state.append("Sobresaliente")
    elif 5 <= average < 8.5:
        state.append("Aceptable")
    elif average < 5:
        state.append("Bajo")
    
    staff.append({
        "Nombre": name,
        "Desempeño semanal": weeks,
        "Estado": state,
        "Promedio": average  
    })
    print("Empleado registrado con exito... ")
        
def performance_staff():
    staff_user = input("Digite el nombre del empleado: ").lower()
    for i in staff:
        if staff_user == i['Nombre'].lower():
            print(f"         Este es el desempeño de {i['Nombre']} ")
            print(f"Desempeño por semana: {i['Desempeño semanal']}  |  Promedio del desempeño: {i['Promedio']}  |  Estado: {i['Estado']}")

def list_autstanding():
    for i in staff:
        if i['Promedio'] >= 8.5:
            print(i)
        else:
            print("No hay empleados con un estado sobresaliente")
            
def report_staff():
    if len(staff) == 0:
        for i in staff:
            print(i)
    else:
        print("No hay empleados registrados... ")








menu = True
while menu:
    print("""
                ________________________________________________
                |                                              |
                |             Corporate Program                |
                |             ---BIENVENIDOS---                |
                |                                              |
                |----------------------------------------------|
                |                                              |
                |  1.Registrar empleados y desempeño laboral   |
                |  2.Desempeño promedio del empleado           |
                |  3.Lista de empleados sobresalientes         |
                |  4.Reporte final de todos los empleados      |
                |  5.Salir                                     |
                |______________________________________________|
                """)
    try:
        option = int(input("\n         Seleccione una opcion: "))
        match option:
            case 1:
               register_data_staff()
            case 2:
                performance_staff()
            case 3:
                list_autstanding()
            case 4:
                report_staff()
            case 5:
                print(""" 
                    ______________________________________________
                    |                                            |
                    |           Que Tenga un Feliz Dia           |
                    |                                            |
                    |           Vuelva Pronto!!!                 |
                    |                                            |
                    |____________________________________________|""")
                menu = False
    except ValueError:
        print("Argumento no valido!!!")
            