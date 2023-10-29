from flask import Flask,jsonify,request
from flask_cors import CORS
from main import Main
from main import Bd

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
        '''MsgConverted = mn.XML_JSO(archivoMSg)'''
        '''print(MsgConverted)'''
        print(archivoMSg)
        return jsonify({'message':"El archivo se recibio exitosamente"})

@app.route('/CargaArchivosConfiguracion',methods=['POST'])
def grabarConfiguracion():
    if request.method == 'POST':
        archivoDiccionario = request.files['archivoDicc']
        mn = Main()
        DiccionarioConverted = mn.XML_JSO(archivoDiccionario)
        print(DiccionarioConverted)
        return jsonify({'message': "El archivo se recibio exitosamente", "Datos": DiccionarioConverted})

@app.route('/LimpiarDatos',methods=['POST'])
def limpiarDatos():
    if request.method == 'POST':
        gg = Bd()
        gg.vaciar()
        return jsonify({'message':"Se han limpiado los datos correctamente"})

@app.route('/devolverHastags',methods=['GET'])
def devolverHastags():
    pass

@app.route('/devolverMenciones',methods=['GET'])
def devolverMenc():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=4000)