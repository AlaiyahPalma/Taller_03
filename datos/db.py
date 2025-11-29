import pymysql

# conexion con la base de datos
connector = pymysql.connect(
  user="root",
  password="",
  host="127.0.0.1",
  port=3306,
  database="practica"
)

cursor = connector.cursor()

query = '''DROP TABLE IF EXISTS proveedor;'''

cursor.execute(query)

query = '''CREATE TABLE proveedor (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  proveedor VARCHAR(100),
  status INT,
  ciudad VARCHAR(150)
);'''

cursor.execute(query)

queryfull = "INSERT INTO proveedor VALUES(null,'Proveedor#21',3,'Chiriqui' )"
cursor.execute(queryfull)

connector.commit()

query1 = "INSERT INTO proveedor VALUES(null,%s,%s,%s)"
values = ('Proveedor#2',2,'Panamá')

cursor.execute(query1,values)
connector.commit()

print("\t++++++Consola de agrega informacion 80++++/n")
nombre = input("Nombre:")
status = int (input("Status: "))
ciudad = input ("Ciudad: ")

datos = (nombre, status, ciudad)

cursor.execute(query1,datos)
connector.commit()

cursor.execute('SELECT * FROM proveedor')

result = cursor.fetchall()
print(result)

data = []

for item in result: 
    id = item[0]
    name = item[1]
    city = item [2]

    lista = {
        "ID": id,
        "nombre": name,
        "ciudad": city
    }
    
    print(lista)

data.append(lista)       