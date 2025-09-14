#Variable
students = []


#Section fuctions

def register_student():
    print("\n            Registrar Estudiante")
    name = input("Nombre del estudiante: ").lower()
    subject = input("Asignatura del estudiante: ").lower()
    subject_note = float(input("Nota del estudiante: "))
    
    students.append({
        "Nombre": name.title(),
        "Asignatura": subject.title(),
        "Nota": subject_note
        })

def list_student():
    if len(students) == 0:
        print("         No hay estudiantes registrados")
    else:
        for student in students:
            print(f"Nombre: {student['Nombre']} Asignatura: {student['Subject_note']} ")

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
            if student[0].lower() == student_select:
                print("         Estudiante encontrado con exito\n")
                print(f"Nombre: {student[0]} | Asignatura: {student[1]} | Nota de la Asignatura {student[2]}")
                found = True
                find = False    
                break
        
        if not found:
            print("         Digite el estudiante tal cual lo registro\n")
            
            
    

    
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
    option = int(input("\n         Seleccione una opcion: "))
    match option:
        case 1:
            register_student()
        case 2:
            list_student()
        case 3:
            find_student()
        case 4:
            None
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