from flask import Flask,jsonify,request
from flask_cors import CORS
from main import Main
from main import Bd
from ER import ER

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello_world():
    return jsonify({'message': 'Funcionando Jefe'})

@app.route('/subirA',methods=['POST'])
def archivo():
    archivo = request.form['Entrada']

@app.route('/entradaMensaje',methods=['POST'])
def grabarMensaje():
    if request.method == 'POST':
        archivoMSg = request.files['archivoMsg']
        bd = Bd()
        bd.anadir(archivoMSg)
        print(archivoMSg)
        return jsonify({'message':"El archivo se recibio exitosamente"})

@app.route('/CargaArchivosConfiguracion',methods=['POST'])
def grabarConfiguracion():
    if request.method == 'POST':
        archivoDiccionario = request.files['archivoDicc']
        bd = Bd()
        bd.anadirDiccionario(archivoDiccionario)
        return jsonify({'message': "El archivo se recibio exitosamente"})

@app.route('/LimpiarDatos',methods=['POST'])
def limpiarDatos():
    if request.method == 'POST':
        gg = Bd()
        gg.vaciar()
        return jsonify({'message':"Se han limpiado los datos correctamente"})

@app.route('/devolverHastags',methods=['GET'])
def devolverHastags():
    mnE = ER()
    mnE.getDatos()
    return jsonify({'message':"Accion realizada con exito"})


@app.route('/devolverMenciones',methods=['GET'])
def devolverMenc():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=7000)