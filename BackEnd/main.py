import json
import xmltodict


class Main():
    def __init__(self):
        pass

    def XML_JSO(self,archivoXMl):
        info = archivoXMl.read()
        XmlObject = xmltodict.parse(info)
        JsonObject = json.dumps(XmlObject)
        return JsonObject


class Bd():
    def __init__(self):
        self.bdPath = "C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/db.xml"
        self.dbDiccionarioPath = "C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/db.xml"

    def vaciar(self):
        with open(self.bdPath,'w') as archivo:
            archivo.write("")

    def anadir(self,archivoXMl):
        infoN = archivoXMl.read()
        infoN_str = infoN.decode()
        sinP = infoN_str[33:-13]
        print(sinP)

        infoAlmacenada = open(self.bdPath,'r').read()
        inforSinE = infoAlmacenada[33:-12]
        print(infoAlmacenada)

        xml = '<?xml version="1.0"?>'
        msjA = '\n<MENSAJES>\n'
        msjC = '\n</MENSAJES>'

        with open(self.bdPath,'w') as archivo:
            archivo.write(xml+msjA+inforSinE+sinP+msjC)

    def anadirDiccionario(self):
        pass