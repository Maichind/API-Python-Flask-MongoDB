from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
import pymongo
import certifi
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

from models.mesas import Mesas
from models.partidos import Partidos
from models.candidatos import Candidatos
from models.resultados import Resultados

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Mind:Mindiola97_@cluster0.ul2xebu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

baseDatos = client["DB-Votaciones"] 
# print(baseDatos.list_collection_names())
@cross_origin
@app.route('/')
def home():
    return jsonify({"mensaje": "APP Votación"})
    #return render_template('index.html')


# ------------- MESAS ----------------------
# Metods: POST
# Opcion para agregar mesas a la base de datos.
@cross_origin
@app.route('/mesas', methods=['POST'])
def addMesa():
    mesa = request.json['mesa']
    cedulas_inscritas = request.json['cedulas_inscritas']

    if mesa and cedulas_inscritas :
        mesaNew = Mesas(mesa,cedulas_inscritas)
        baseDatos.mesas.insert_one(mesaNew.toDBCollection())
        response = jsonify({
            "mesa": mesa,
            "cedulas_inscritas": cedulas_inscritas
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todas las mesas registradas.
@cross_origin
@app.route('/mesas', methods=['GET'])
def getMesas():
    mesas = baseDatos.mesas.find()
    response = json_util.dumps(mesas)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de una mesa registrada por su id.
@cross_origin
@app.route('/mesas/<id>', methods=['GET'])
def getMesa(id):
    mesa = baseDatos.mesas.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(mesa)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de una mesa por su id.
@cross_origin
@app.route('/mesas/update/<id>', methods=['PUT'])
def updateMesa(id):
    mesa = request.json['mesa']
    cedulas_inscritas = request.json['cedulas_inscritas']

    if mesa and cedulas_inscritas:
        baseDatos.mesas.update_one({"_id": ObjectId(id)}, {'$set' : 
                                    {'mesa' : mesa, 'cedulas_inscritas' : cedulas_inscritas}})
        response = jsonify({'message' : 'Mesa ' + id + ' actualizada correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar una mesa por su id.
@cross_origin
@app.route('/mesas/delete/<id>', methods=['DELETE'])
def deleteMesa(id):
    baseDatos.mesas.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Mesa '+ id +' borrada correctamente'})


# ------------- PARTIDOS ----------------------
# Metods: POST
# Opcion para agregar partidos a la base de datos.
@cross_origin
@app.route('/partidos', methods=['POST'])
def addPartido():
    nombrePartido = request.json['nombrePartido']
    lema = request.json['lema']

    if nombrePartido and lema :
        partidoNew = Partidos(nombrePartido,lema)
        baseDatos.partidos.insert_one(partidoNew.toDBCollection())
        response = jsonify({
            "nombrePartido": nombrePartido,
            "lema": lema
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los partidos registrados.
@cross_origin
@app.route('/partidos', methods=['GET'])
def getPartidos():
    partidos = baseDatos.partidos.find()
    response = json_util.dumps(partidos)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un partido registrado por su id.
@cross_origin
@app.route('/partidos/<id>', methods=['GET'])
def getPartido(id):
    partido = baseDatos.partidos.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(partido)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un partido por su id.
@cross_origin
@app.route('/partidos/update/<id>', methods=['PUT'])
def updatePartido(id):
    nombrePartido = request.json['nombrePartido']
    lema = request.json['lema']

    if nombrePartido and lema:
        baseDatos.partidos.update_one({"_id": ObjectId(id)}, {'$set' : 
                                    {'nombrePartido' : nombrePartido, 'lema' : lema}})
        response = jsonify({'message' : 'Partido ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un partido por su id.
@cross_origin
@app.route('/partidos/delete/<id>', methods=['DELETE'])
def deletePart(id):
    baseDatos.partidos.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Partido '+ id +' borrado correctamente'})


# ------------- CANDIDATOS ----------------------
# Metods: POST
# Opcion para agregar candidatos a la base de datos.
@cross_origin
@app.route('/candidatos', methods=['POST'])
def addCandidato():
    numero = request.json['numero']
    cedula = request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    partido = request.json['partido']
    segundaVuelta = request.json['segundaVuelta']

    if numero and cedula and nombre and apellido and partido and segundaVuelta:
        candidatoNew = Candidatos(numero, cedula, nombre, apellido, partido, segundaVuelta)
        baseDatos.candidatos.insert_one(candidatoNew.toDBCollection())
        response = jsonify({
            "numero": numero,
            "cedula,": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "partido": partido,
            "segundaVuelta": segundaVuelta
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los candidatos registrados.
@cross_origin
@app.route('/candidatos', methods=['GET'])
def getCandidatos():
    candidatos = baseDatos.candidatos.find()
    response = json_util.dumps(candidatos)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un candidato registrado por su id.
@cross_origin
@app.route('/candidatos/<id>', methods=['GET'])
def getCandidato(id):
    candidato = baseDatos.candidatos.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(candidato)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un candidato por su id.
@cross_origin
@app.route('/candidatos/update/<id>', methods=['PUT'])
def updateCandidato(id):
    numero = request.json['numero']
    cedula = request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    partido = request.json['partido']
    segundaVuelta = request.json['segundaVuelta']

    if numero and cedula and nombre and apellido and partido and segundaVuelta:
        baseDatos.candidatos.update_one({"_id": ObjectId(id)}, {'$set' : 
                                        {'numero' : numero, 'cedula' : cedula, 'nombre' : nombre, 
                                        'apellido' : apellido, 'partido' : partido, 'segundaVuelta': segundaVuelta}})
        response = jsonify({'message' : 'Candidato ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un candidato por su id.
@cross_origin
@app.route('/candidatos/delete/<id>', methods=['DELETE'])
def deleteCand(id):
    baseDatos.candidatos.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Candidato '+ id +' borrado correctamente'})


# ------------- RESULTADOS ----------------------
# Metods: POST
# Opcion para agregar resultados a la base de datos.
@cross_origin
@app.route('/resultados', methods=['POST'])
def addResultado():
    mesa = request.json['mesa']
    nombre = request.json['nombre']
    votos = request.json['votos']
    nombre2 = request.json['nombre2']
    votos2 = request.json['votos2']

    if mesa and nombre and votos and nombre2 and votos2:
        resultadoNew = Resultados(mesa, nombre, votos, nombre2, votos2)
        baseDatos.resultados.insert_one(resultadoNew.toDBCollection())
        response = jsonify({
            "mesa": mesa,
            "nombre": nombre,
            "votos": votos,
            "nombre2": nombre2,
            "votos": votos2
        })
        return response
    return notFound()

# Metods: GET
# Opcion para obtener los datos todos los partidos registradas.
@cross_origin
@app.route('/resultados', methods=['GET'])
def getResultados():
    resultados = baseDatos.resultados.find()
    response = json_util.dumps(resultados)
    return Response (response, mimetype='application/json')

# Opcion para obtener los datos de un partido registrado por su id.
@cross_origin
@app.route('/resultados/<id>', methods=['GET'])
def getResultado(id):
    resultado = baseDatos.resultados.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(resultado)
    return Response (response, mimetype='application/json')

# Metods: PUT
# Opcion para actualizar los datos de un resultado por su id.
@cross_origin
@app.route('/resultados/update/<id>', methods=['PUT'])
def updateResultado(id):
    mesa = request.json['mesa']
    nombre = request.json['nombre']
    votos = request.json['votos']
    nombre2 = request.json['nombre2']
    votos2 = request.json['votos2']

    if mesa and nombre and votos and nombre2 and votos2:
        baseDatos.resultados.update_one({"_id": ObjectId(id)}, {'$set' : 
                                        {'mesa' : mesa, 'nombre' : nombre, 'votos' : votos, 
                                        'nombre2' : nombre2, 'votos2' : votos2}})
        response = jsonify({'message' : 'Resultado ' + id + ' actualizado correctamente'})
        return response
    return notFound()

# Metods: DELETE
#Opción para eliminar un resultado por su id.
@cross_origin
@app.route('/resultados/delete/<id>', methods=['DELETE'])
def deleteRes(id):
    baseDatos.resultados.delete_one({"_id": ObjectId(id)})
    return jsonify({'message' : 'Resultado '+ id +' borrado correctamente'})


#----------------ERROR-----------------------
@cross_origin
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=9999)