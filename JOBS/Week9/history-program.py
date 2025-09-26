#   Variables

cities = [
    {"Departamento": "Bogota",
     "2018": 7830,
     "2019": 7900,
     "2020": 7970,
     "2021": 8050,
     "2022": 8120
     },
    
    {"Departamento": "Antioquia",
     "2018": 6420,
     "2019": 6480,
     "2020": 6535,
     "2021": 6590,
     "2022": 6650
     },
    
    {"Departamento": "Valle del cauca",
     "2018": 4500,
     "2019": 4540,
     "2020": 4580,
     "2021": 4620,
     "2022": 4670
     }
]
#   FUNCIONES DEL PROGRAMA

# 1. Calcular la tasa de crecimiento compuesto anual
def estimate_increase():
    while True:
        n1 = 4   # Intervalo de años (de 2018 a 2022 → 4 años)
        
        # Se pide al usuario un departamento
        user = input("Digite la ciudad que desea consultar...\n-Bogota\n-Antioquia\n-Valle del cauca\n           : ").lower()

        for i in cities: 
            # Verificamos si coincide lo digitado con el nombre en la base de datos
            if user == i['Departamento'].lower():
                p_initial = i['2018']   # Población inicial (año 2018)
                p_end = i['2022']       # Población final (año 2022)
                
                # Fórmula del crecimiento compuesto:
                # (P_final / P_inicial)^(1/n) - 1
                result = (p_end / p_initial) ** (1 / n1) - 1 
                
                # Convertimos a porcentaje
                result_percent = result * 100   
                
                # Imprimimos con dos decimales
                print(f"Tasa de crecimiento: {result_percent:.2f}%")
                
        # Preguntamos si quiere seguir consultando
        option = input("\n¿Desea consultar otro departamento?(si/no): ").lower()
        if option != "si":                
            break      

# 2. Proyección de la población a 5 años
def proyection_poblate():
    while True:
        n1 = 4   # Intervalo de años (2018 a 2022)
        
        user = input("Digite la ciudad que desea consultar...\n-Bogota\n-Antioquia\n-Valle del cauca\n           : ").lower()

        for i in cities: 
            if user == i['Departamento'].lower():
                p_initial = i['2018']
                p_end = i['2022']
                
                # Tasa de crecimiento compuesta
                result = (p_end / p_initial) ** (1 / n1) - 1 
                result_percent = result * 100   
                
                print("Proyección para los próximos 5 años..\n ")
                
                # Proyectamos desde 2023 hasta 2027
                for t in range(1,6):
                    proyection = p_end * (1 + result) ** t
                    print(f"Año {2022 + t}: {proyection:.0f} mil habitantes")
        
        option = input("\n¿Desea consultar otro departamento?(si/no): ").lower()
        if option != "si":                
            break   

# 3. Análisis cualitativo de los factores poblacionales
def analysis_city():
    while True:
        # Menú numérico para seleccionar ciudad
        user = int(input("          Digite la ciudad que desea consultar...\n1.Bogota\n2.Antioquia\n3.Valle del cauca\n: "))
        
        if user == 1:
            print("""
            Bogota
        El crecimiento poblacional de Bogotá entre 2018 y 2022 estuvo marcado por la llegada
        de migrantes venezolanos y de otras regiones del país, atraídos por las oportunidades
        laborales, educativas y de servicios. La mejora en la cobertura de salud y programas
        sociales también favoreció la permanencia de la población. No obstante, factores como
        el alto costo de vida y las dificultades derivadas de la pandemia de COVID-19 moderaron
        este crecimiento.      
                  """)
        elif user == 2:
            print("""
            Antioquia
        En Antioquia, el dinamismo económico y el desarrollo de Medellín como polo de innovación
        y empleo impulsaron la llegada de población tanto nacional como extranjera. Sin embargo,
        fenómenos como el desplazamiento forzado por la violencia en zonas rurales y los efectos
        negativos de la pandemia limitaron en parte el aumento poblacional en el departamento.  
                  """)
        elif user == 3:
            print("""
            Valle del Cauca
        El Valle del Cauca, con Cali como su principal centro urbano, experimentó crecimiento 
        poblacional gracias a la migración interna desde zonas rurales y a la llegada de migrantes
        extranjeros. La urbanización y el atractivo económico de la región fueron claves en este
        proceso. Aun así, la violencia en algunos territorios, la desigualdad social y el impacto
        de la pandemia de COVID-19 influyeron de forma negativa en su ritmo de crecimiento.      
                  """)
        else:
            print("Argumento no valido!!!")

# 4. Visualización gráfica de los datos históricos
def graph():
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Datos de cada región (coherentes con la lista cities)
    bogota = {"2018": 7830, "2019": 7900, "2020": 7970, "2021": 8050, "2022": 8120}
    antioquia = {"2018": 6420, "2019": 6480, "2020": 6535, "2021": 6590, "2022": 6650}
    valle = {"2018": 4500, "2019": 4540, "2020": 4580, "2021": 4620, "2022": 4670}

    # Años → claves
    años = list(bogota.keys())
    
    # Valores de población por región
    bogota_vals = list(bogota.values())
    antioquia_vals = list(antioquia.values())
    valle_vals = list(valle.values())

    # Estilo visual de seaborn
    sns.set(style="whitegrid")

    # Crear gráfico de líneas
    plt.figure(figsize=(8,5))
    plt.plot(años, bogota_vals, marker="o", label="Bogotá")
    plt.plot(años, antioquia_vals, marker="o", label="Antioquia")
    plt.plot(años, valle_vals, marker="o", label="Valle del Cauca")

    # Personalización del gráfico
    plt.title("Evolución de la Población por Región (2018–2022)")
    plt.xlabel("Año")
    plt.ylabel("Población (miles)")
    plt.legend()
    plt.show()

#   MENÚ PRINCIPAL

menu = True
while menu:
    # Menú de opciones
    print("""
                _____________________________________________
                |                                           |
                |         Population Analysis System        |
                |             ---BIENVENIDOS---             |
                |                                           |
                |-------------------------------------------|
                |                                           |
                |  1. Tasa de crecimiento compuesto         |
                |  2. Proyeccion de poblacion               |
                |  3. Visualizacion grafica                 |
                |  4. Analisis adicional                    |
                |  5. Salir                                 |
                |___________________________________________|
                """)
    try:
        option = int(input("\n         Seleccione una opcion: "))
        
        # Estructura match-case (similar a switch en otros lenguajes)
        match option:
            case 1:
                estimate_increase()
            case 2:
                proyection_poblate()
            case 3:
                graph()    
            case 4:
                analysis_city()
            case 5:
                # Mensaje de salida
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
        # Si el usuario mete algo no numérico
        print("Argumento no valido!!!")
