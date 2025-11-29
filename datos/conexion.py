import pymysql

def getConnexion():
    connector = pymysql.connect(
        
    user="root",
    password="",
    host="127.0.0.1",
    port=3306,
    database="practica"
    )
    return connector

def getCursor():
    cursor = getConnexion().cursor()
    return cursor 

def getEntidad(nombre):
    cursor = getCursor()
    query = "SELECT * FROM {}".format(nombre)

    print ("Quary: ", query)
    cursor.execute(query)
    result = cursor.fetchall()

    return result

print(getEntidad('proveedor'))

testData =getEntidad('proveedor')
print(testData)

def addProveedor():...

...
