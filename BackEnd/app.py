from flask import Flask,jsonify,request,send_file
from flask_cors import CORS
from main import Main
from main import Bd
from ER import ER
from GETS import Hastags,Menciones,Sentimientos

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
        archivoMSg = request.form['archivoMsg']
        bd = Bd()
        unido = bd.anadir(archivoMSg)
        ArchivoTemp = open("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/Temporal.xml", "w")
        ArchivoTemp.write(unido)
        ArchivoTemp.close()
        print(archivoMSg)
        return send_file('C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/Temporal.xml')

@app.route('/CargaArchivosConfiguracion',methods=['POST'])
def grabarConfiguracion():
    if request.method == 'POST':
        archivoDiccionario = request.form['archivoDicc']
        bd = Bd()
        bd.anadirDiccionario(archivoDiccionario)
        return jsonify({'message': "El archivo se recibio exitosamente"})

@app.route('/LimpiarDatos',methods=['POST'])
def limpiarDatos():
    if request.method == 'POST':
        gg = Bd()
        gg.vaciar()
        return jsonify({'message':"Se han limpiado los datos correctamente"})

@app.route('/devolverHastags',methods=['POST'])
def devolverHastags():
    if request.method == 'POST':
        mnE = ER()
        PrimerRango = request.form['PrimerRango']
        SegundoRango = request.form['SegundoRango']
        DiccionarioConDatos = mnE.getDatos()
        hash = Hastags(DiccionarioConDatos,PrimerRango,SegundoRango)
        Filtrado = hash.filtar()
        return Filtrado


@app.route('/devolverMenciones',methods=['POST'])
def devolverMenc():
    if request.method == 'POST':
        mnE = ER()
        PrimerRango = request.form['PrimerRango']
        SegundoRango = request.form['SegundoRango']
        DiccionarioConDatos = mnE.getDatos()
        menciones = Menciones(DiccionarioConDatos,PrimerRango,SegundoRango)
        MenciFilt = menciones.filtrarMenciones()
        return MenciFilt

@app.route('/devolverSentimientos',methods=['POST'])
def devolverSentimientos():
    if request.method == 'POST':
        mnE = ER()
        PrimerRango = request.form['PrimerRango']
        SegundoRango = request.form['SegundoRango']
        DiccionarioConDatos = mnE.getDatos()
        sentimientos = Sentimientos(DiccionarioConDatos,PrimerRango,SegundoRango)
        SentiFiltPosi,SentiFiltNega = sentimientos.filtrarSentimientos()
        return SentiFiltPosi,SentiFiltNega

if __name__ == '__main__':
    app.run(debug=True, port=7000)