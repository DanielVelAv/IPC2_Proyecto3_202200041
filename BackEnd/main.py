import json
import xmltodict
import lxml.etree as ETR
import xml.etree.ElementTree as ET


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
        self.dbDiccionarioPath = "C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml"

    def vaciar(self):
        with open(self.bdPath,'w') as archivo:
            archivo.write("")

        concatenadoDicc = "<diccionario>\n"
        concatenadoDicc += "<sentimientos_positivos>\n\n"
        concatenadoDicc += "</sentimientos_positivos>\n\n"
        concatenadoDicc += "<sentimientos_negativos>\n\n"
        concatenadoDicc += "</sentimientos_negativos>\n\n"
        concatenadoDicc += "<positivas_rechazadas>\n\n"
        concatenadoDicc += "</positivas_rechazadas>\n\n"
        concatenadoDicc += "<negativas_rechazadas>\n\n"
        concatenadoDicc += "</negativas_rechazadas>\n\n"
        concatenadoDicc += "</diccionario>"


        with open(self.dbDiccionarioPath,"w") as files:
            files.write(concatenadoDicc)

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

    def anadirDiccionario(self,archivoDiccionario):

        InforDiccionarioCompleto = archivoDiccionario.read()
        infoArreglada = InforDiccionarioCompleto.decode()
        listadoPalabrasPositivas = ""

        baseDatosDiccionarios = ET.parse("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")

        print(infoArreglada)
        infoIntento = ET.fromstring(infoArreglada)
        for i in infoIntento.findall('sentimientos_positivos'):
            for j in i.findall('palabra'):
                palabraPositiva = j.text
                palabra = ET.Element("palabra")
                palabra.text = palabraPositiva
                print(palabraPositiva)
                VF = self.VerificarExistePositivos(palabraPositiva)
                VFEP = self.VerificarExisteNegativos(palabraPositiva)
                VFER = self.verificarExisteRechazdas(palabraPositiva)
                VFEOL = self.verificarExisteArchivoN(palabraPositiva,infoIntento)
                if VF:
                    print("Ya se encuentra")
                elif VF == False and VFEP == False and VFER == False and VFEOL == False:
                    baseDatosDiccionarios.getroot().find("sentimientos_positivos").append(palabra)
                    baseDatosDiccionarios.write("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")
                else:
                    baseDatosDiccionarios.getroot().find("positivas_rechazadas").append(palabra)
                    baseDatosDiccionarios.write("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")

        for k in infoIntento.findall('sentimientos_negativos'):
            for l in k.findall('palabra'):
                palabraNegativa = l.text
                palabra2 = ET.Element("palabra")
                palabra2.text = palabraNegativa
                VF = self.VerificarExisteNegativos(palabraNegativa)
                VFEN = self.VerificarExistePositivos(palabraNegativa)
                VFER = self.verificarExisteRechazdas(palabraNegativa)
                VFEOP = self.verificarExisteArchivoP(palabraNegativa, infoIntento)
                if VF:
                    print("Ya se encuentra")
                elif VF == False and VFEN == False and VFER == False and VFEOP == False:
                    baseDatosDiccionarios.getroot().find("sentimientos_negativos").append(palabra2)
                    baseDatosDiccionarios.write("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")
                else:
                    baseDatosDiccionarios.getroot().find("negativas_rechazadas").append(palabra2)
                    baseDatosDiccionarios.write("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")



    def VerificarExistePositivos(self,palabra):
        Estado = False
        bd = ET.parse(self.dbDiccionarioPath).getroot()
        for i in bd.findall("sentimientos_positivos"):
            for j in i.findall("palabra"):
                if j.text == palabra:
                    print("gg", j.text)
                    Estado = True
                else:
                    pass
        return Estado

    def VerificarExisteNegativos(self,palabra2):
        Estado = False
        bd = ET.parse(self.dbDiccionarioPath).getroot()
        for i in bd.findall("sentimientos_negativos"):
            for j in i.findall("palabra"):
                if j.text == palabra2:
                    print("gg", j.text)
                    Estado = True
                else:
                    pass
        return Estado

    def verificarExisteRechazdas(self,palabra3):
        Estado = False
        bd = ET.parse(self.dbDiccionarioPath).getroot()
        for i in bd.findall("negativas_rechazadas"):
            for j in i.findall("palabra"):
                if j.text == palabra3:
                    print("gg", j.text)
                    Estado = True
                else:
                    pass
        return Estado

    def verificarExisteArchivoN(self,palabra4,info):
        Estate = False
        for h in info.findall("sentimientos_negativos"):
            for t in h.findall("palabra"):
                if t.text == palabra4:
                    Estate = True
                else:
                    pass
        return Estate

    def verificarExisteArchivoP(self,palabra5,info):
        Estate = False
        for h in info.findall("sentimientos_positivos"):
            for t in h.findall("palabra"):
                if t.text == palabra5:
                    Estate = True
                else:
                    pass
        return Estate