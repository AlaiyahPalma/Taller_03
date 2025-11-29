from flask import Flask
from flask import request, jsonify
from datos.conexion import *

app = Flask(__name__)

@app.route('/')
def home():
    info = getEntidad("proveedor")
    return jsonify(info)

@app.route('/add', methods=['POST'])
def add():
    nombre = request.json['proveedor']
    status = request.json['status']
    ciudad = request.json['ciudad']
    addProveedor(nombre, status, ciudad)
    return jsonify({"mensaje": "Proveedor agregado"})

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    nombre = request.json['proveedor']
    status = request.json['status']
    ciudad = request.json['ciudad']
    updateProveedor(id, nombre, status, ciudad)
    return jsonify({"mensaje": "Proveedor actualizado"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    deleteProveedor(id)
    return jsonify({"mensaje": "Proveedor eliminado"})

if __name__ == '__main__':
    app.run(debug=True)

    