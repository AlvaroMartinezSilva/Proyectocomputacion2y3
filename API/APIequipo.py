#!bin/python

# API que pasandole un texto haga analisis de sentimiento, usando textblop o algo asi, con libreria de traduccion para que funcione traducion del español al ingles
# from importlib.resources import path
# import os
# from flask import Flask, jsonify, request, abort, make_response

# app = Flask(__name__)

# url = 'Grupo_7.PC1.Act4\Doc\NoOdio/20MinutosNoOdioRM_0.txt'

# texto = os.path.join(url, '20MinutosNoOdioRM_0.txt')

# @app.route('/analisis', methods = ['GET'])
# def texto_analisis():
#     return texto

from flask import Flask, jsonify, abort, request, make_response, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
# CORS(app, origins="http://localhost:4200", allow_headers=[
#     "Content-Type", "Authorization", "Access-Control-Allow-Credentials","Access-Control-Allow-Origin"],
#     supports_credentials=True, intercept_exceptions=False)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/analisis', methods = ['POST'])
def sentiment_analyzer_scores(sentence):
    score = SentimentIntensityAnalyzer.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

# def create_texto():
#     if not request.json or not 'cuerpo' in request.json:
#         abort(400)
#     texto = {
#         'cuerpo': request.json['cuerpo'],
#     }

#     sentence = texto['cuerpo']
#     analyzer = SentimentIntensityAnalyzer().polarity_scores(sentence)
#     print(analyzer)
#     return jsonify(analyzer), 201
    
if __name__ == '__main__':
    app.run(debug = True)