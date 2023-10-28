from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=[''])
def hello_world():
    return jsonify({'message': 'Prueba Post'})

@app.route('/prueba',methods=['GET'])
def prueba():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        passw = request.form['txtPassword']

        return jsonify({'message': 'usuario Agregado', 'nombre': nombre, 'contraseña': passw})

@app.route('/pruebabybody',methods=['GET'])
def byBody():
    micurso = request.json['curso']
    miseccion = request.json['seccion']
    return jsonify({'message': 'Curso Agregado', 'curso':micurso, 'secion': miseccion})

@app.route('/subirA',methods=['POST'])
def archivo():
    archivo = request.form['Entrada']

@app.route('/grabarMensaje',methods=['POST'])
def grabarMensaje():
    pass

@app.route('/grabarConfiguracion',methods=['POST'])
def grabarConfiguracion():
    pass

@app.route('/LimpiarDatos',methods=['POST'])
def limpiarDatos():
    pass

@app.route('/devolverHastags',methods=['POST'])
def devolverHastags():
    pass

@app.route('/devolverMenciones',methods=['POST'])
def devolverMenc():
    pass

if __name__ == '__main__':
    app.run(debug=True)