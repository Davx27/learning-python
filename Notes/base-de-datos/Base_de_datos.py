import sqlite3
conn = sqlite3.connect('test-data')
queryy = '''
DROP TABLE if exists personas
'''
query = '''
CREATE TABLE if not exists personas
(ID         INT PRIMARY KEY NOT NULL,
nombre      TEXT            NOT NULL,
edad        INT             NOT NULL,
descripcion TEXT            NOT NULL,
fecha       TEXT            NOT NULL)
'''
conn.execute(query)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall( ))


conn.commit()
conn.close()