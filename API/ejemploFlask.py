#!bin/python

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

#Variable estilo json
actividades = [
    {
        'id': 1,
        'titulo': 'Mi primera actividad'
    },
    {
        'id': 2,
        'titulo': 'Mi segunda actividad'
    },
]

#ENDPOINTS

#Devuelve variable definida como json
@app.route('/actividades', methods = ['GET'])
def get_actividades():
    return jsonify({'actividades': actividades})

#Permite elegir lo que queremos dentro del json
@app.route('/actividades/<int:id>', methods = ['GET'])
def get_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if (len(actividad) == 0):
        return make_response(jsonify({ 'error': 'Actividad no encontrada'}), 404) #Opcion 1
    return jsonify({'actividad': actividad[0]})

#Insertamos nuevas actividades en el array
@app.route('/actividades', methods=['POST'])
def create_actividad():
    if not 'titulo' in request.json:
        abort (404) #Opcion 2
    actividad = {
        'id' : actividades[-1]['id'] + 1,
        'titulo' : request.json['titulo']
    }
    actividades.append(actividad)
    return jsonify( {'actividad': actividad})

#Borrar actividad
@app.route('/actividades/<int:id>', methods = ['DELETE'])
def delete_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if (len(actividad) == 0):
        return "ERROR" #Opcion 3
    actividades.remove(actividad[0])
    return jsonify({'result': 'Actividad eliminada'})

#Devuelve texto plano
@app.route('/', methods = ['GET'])
def inicio():
    return "Hola, soy tu primera API"

#INICIA LA APLICACIÓN
if __name__ == '__main__':
    app.run(debug = True)