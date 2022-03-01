#!bin/python
from flask import Flask,jsonify,request


app=Flask(__name__)



actividades=[
{'id':1,
'titulo':'Mi primera actividad'},
{'id':2,
'titulo':'Mi segunda actividad'}

]



@app.route('/actividades',methods=['GET'])

def get_actividades():
    return jsonify({'actividades':actividades})


@app.route('/actividades/<int:id>',methods=['GET'])

def get_actividad(id):
    actividad =list(filter(lambda t:t['id']==id,actividades))
    if (len(actividad)==0):
        return "ERROR"
    return jsonify({'actividad':actividad[0]})


@app.route('/actividades/<int:id>',methods=['DELETE'])

def delete_actividad(id):
    actividad =list(filter(lambda t:t['id']==id,actividades))
    if (len(actividad)==0):
        return "ERROR"
    actividades.remove(actividad[0])
    return jsonify({'result':'Actividad eliminada'})


@app.route('/actividades/<int:id>',methods=['POST'])

def create_actividad():
    if not 'titulo' in request.json:
        return "ERROR"
    actividad ={
        'id':actividades[-1]['id']+1,
        'titulo':request.json['titulo']


    }
    actividades.append(actividad)
    return jsonify ({'actividad':actividad})



@app.route('/',methods=['GET'])

def inicio():
    return "Hola soy tu primera API"

if __name__=='__main__':
    app.run(debug=True)

    