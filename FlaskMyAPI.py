#!bin/python

#from urllib import request
from flask import Flask, jsonify, request, abort, make_response

#Bucle del servidor
app = Flask(__name__)

#funciones personalizadas

#pip install sentiment-analysis-spanish
#pip install keras tensorflow
from sentiment_analysis_spanish import sentiment_analysis
def emocional(texto):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    sentimiento = sentiment.sentiment(texto)
    
    return sentimiento

#Funciones ENDPOINTS

actividades = [
    {
        'id': 1,
        'titulo': 'Mi actividad 1'
    },
    {
        'id': 2,
        'titulo': 'Mi actividad 2'
    },
]
@app.route('/actividades', methods = ['GET'])
def get_actividades():
    return jsonify( {'actividades': actividades })

@app.route('/actividades', methods = ['POST'])
def create_actividad():
    if not 'titulo' in request.json:
        return "ERROR"
    actividad = {
        'id': actividades[-1]['id'] + 1,
        'titulo': request.json['titulo']
    }
    actividades.append(actividad)
    return jsonify( {'actividad': actividad })

@app.route('/actividades/<int:id>', methods = ['GET'])
def get_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if len(actividad) == 0:
        return make_response(jsonify({ 'error': 'Actividad no encontrada'}), 404)
    return jsonify( {'actividad': actividad[0]})

@app.route('/actividades/<int:id>', methods = ['DELETE'])
def delete_actividad(id):
    actividad = list(filter(lambda t: t['id'] == id, actividades))
    if len(actividad) == 0:
        return "ERROR"
    actividades.remove(actividad[0])
    return jsonify( {'result': 'Actividad '+ str(id) +' eliminada' })

@app.route('/sentimiento', methods = ['POST'])
def sentimental():
    if not 'texto' in request.json:
        return "ERROR"
    texto = request.json['texto']
    sentimiento = emocional(texto)
    analisis = {
        'texto': texto,
        'sentimiento': sentimiento
    }
    return jsonify( {'analisis': analisis })


#Pordefecto
@app.route('/', methods = ['GET'])
def inicio():
    return "Hola, soy tu primera API"


if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = True, host='0.0.0.0', port=80)