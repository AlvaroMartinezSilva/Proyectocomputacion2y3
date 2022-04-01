#!bin/python

#from urllib import request
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS, cross_origin#CORs $pip install -U flask-cors

#Bucle del servidor
app = Flask(__name__)
CORS(app)#CORs

#funciones personalizadas

#pip install sentiment-analysis-spanish
#pip install keras tensorflow
from sentiment_analysis_spanish import sentiment_analysis
def emocional(texto):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    sentimiento = sentiment.sentiment(texto) #[0,1]
    carita = ":|"
    if sentimiento > 0.6:
        carita = ":)"
    elif sentimiento < 0.4:
        carita = ":("
    
    return sentimiento, carita

#Funciones ENDPOINTS

@app.route('/sentimiento', methods = ['POST'])
def sentimental():
    if not 'texto' in request.json:
        return "ERROR"
    texto = request.json['texto']
    sentimiento = emocional(texto)
    analisis = {
        'texto': texto,
        'sentimiento': sentimiento[0],
        'carita': sentimiento[1]
    }
    return jsonify( {'analisis': analisis })

@app.route('/saludo', methods = ['GET'])
def saludo():
    return jsonify( {'saludo': 'Hola, ya estoy conectada' })

#Pordefecto
@app.route('/', methods = ['GET'])
def inicio():
    return "Hola, soy tu primera API"


if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = True, host='0.0.0.0', port=80)

#Para el CORs https://stackoverflow.com/questions/28461001/python-flask-cors-issue#:~:text=Flask%20has%20the%20flask%2Dcors%20module.%20Following%20is%20the%20code%20snippet%20as%20well%20as%20the%20procedure.