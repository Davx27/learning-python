#Variable
students = []


#Section fuctions

def register_student():
    add = True
    print("\n            Registrar Estudiante")
    while add:
        name = input("Nombre del estudiante: ").lower()
        exists = False
        for student in students:
            if name == student['Nombre'].lower():
                print("Ya se ha asignado un estudiante con el mismo nombre")
                exists = True
                break
        if exists:
            continue
            
        subject = input("Asignatura del estudiante: ").lower()
        while True:
            try:
                subject_note = float(input("Nota del estudiante: "))    
                if 0 <= subject_note <= 5:
                    break
                else:
                    print("Nota no valida.\nLas notas son de 0.0 a 5.0")
            except ValueError:
                print("Argumento no valido!!!")    
                
                
        students.append({
            "Nombre": name.title(),
            "Asignatura": subject.title(),
            "Nota": subject_note
            })
        print("Estudiante registrado con exito!")
        exituser = input("¿Desea registrar otro estudiante? (SI/NO): ").lower()
        if exituser != "si":
            add = False

def list_student():
    if len(students) == 0:
        print("         No hay estudiantes registrados")
    else:
        for student in students:
            print(f"Nombre: {student['Nombre']} | Asignatura: {student['Asignatura']} | Nota {student['Nota']} ")

def find_student():
    find = True
    while find:
        print("         Buscar esudiante")
        if len(students) == 0:
            print("         No hay estudiantes registrados")
            return
        
        student_select = input("Escriba el estudiante: ").lower()
        found = False
        for student in students:
            if student['Nombre'].lower() == student_select:
                print("         Estudiante encontrado con exito\n")
                print(f"Nombre: {student['Nombre']} | Asignatura: {student['Asignatura']} | Nota de la Asignatura {student['Nota']}")
                found = True
                find = False    
                break
        
        if not found:
            print("         Digite el estudiante tal cual lo registro\n")
            
def calculate_average():
    if len(students) == 0:
        print("         No hay estudiantes registrados")
        return
    print("Calcular promedio de las calificaciones...\n")
    notes = [student['Nota'] for student in students]
    average = sum(notes) / len(notes)
    print(f"El promedio de notas de los estudiantes: {average} ")
    

    
    
    
        
        

    
menu = True
while menu:
        
    print("""
            _____________________________________________
            |                                           |
            |             Student Program               |
            |             ---BIENVENIDOS---             |
            |                                           |
            |-------------------------------------------|
            |                                           |
            |  1.Registrar Estudiante                   |
            |  2.Lista de Estudiantes                   |
            |  3.Buscar Estudiante por nombre           |
            |  4.Calcular Promedio de Calificaciones    |
            |  5.Salir del sistema                      |
            |                                           |
            |___________________________________________|
            """)
    try:
        option = int(input("\n         Seleccione una opcion: "))
        match option:
            case 1:
                register_student()
            case 2:
                list_student()
            case 3:
                find_student()
            case 4:
                calculate_average()
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
        