# 5 funciones -Crear la tabla -Leer todos los elementos -Insertar un elemto en una tabla -Actualizar primer elemento de la tabla -Borrar el ultimo elemento de la tabla
import sqlite3 as sql

def createTable(): #Crear la tabla con sus respectivos valores
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE empleados (
        name    text,
        age     int,
        antiquity_age   int
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(name, age, antiquityAge): #Insertar datos a la tabla
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instuction = f"INSERT INTO empleados VALUES ('{name}', {age}, {antiquityAge})"
    cursor.execute(instuction) 
    conn.commit()
    conn.close()

def readRows(): #Mostrar la lista de los empleados disponibles
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instuction = f"SELECT * FROM empleados"
    cursor.execute(instuction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

def insertRows(empleadosList): #Insertar datos segun una lista de diccionarios
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instuction = f"INSERT INTO empleados VALUES (?, ?, ?)"
    cursor.executemany(instuction, empleadosList) 
    conn.commit()
    conn.close()
    
def readOrdered(field):
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instuction = f"SELECT * FROM empleados ORDER BY {field} DESC" # 'DESC' sirve para cambiar el sentido del orden 
    cursor.execute(instuction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

def search():
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM empleados WHERE name='aljeo'" # name like '?'  Sirve para seleccionar un item de la tabla sin importar si esta en miniscula o mayuscula
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)
    
def upateFields():
    conn = sql.connect("empleados.db")
    cursor = conn.cursor()
    instruction = f"UPDATE empleados SET name='alejo' WHERE name like 'aljeo' " #Modificar datos de la tabla segun el item que quiera
    cursor.execute(instruction)
    
    conn.commit()
    conn.close()
    
def deleteRow():
    conn = sql.connect("empleados.db")
    cursor = conn.cursor
    instruction = f"DELETE FROM empleados WHERE name=''"
    cursor.execute(instruction)
    
    conn.commit()
    conn.close()
    
empleados = [
        ("juan", 28, 7),
        ("alberto", 23, 2),
        ("patricia", 43, 12)
    ]

if __name__ == "__main__":
    #createTable()
    #insertRow("aljeo", 17, 2)
    #insertRow("david", 18, 1)
    #readRows()

    #insertRows(empleados)
    #readOrdered("name")
    #search()
    upateFields()