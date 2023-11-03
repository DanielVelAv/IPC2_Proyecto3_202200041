import json

import unidecode
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
        infoN = archivoXMl
        infoN_str = infoN
        sinP = infoN_str[33:-11]
        print(sinP)

        infoAlmacenada = open(self.bdPath,'r').read()
        inforSinE = infoAlmacenada[33:-11]
        print(infoAlmacenada)

        xml = '<?xml version="1.0"?>'
        msjA = '\n<MENSAJES>\n'
        msjC = '\n</MENSAJES>'

        with open(self.bdPath,'w') as archivo:
            archivo.write(xml+msjA+unidecode.unidecode(inforSinE)+unidecode.unidecode(sinP)+msjC)

        txtParseado = ET.fromstring(archivoXMl)
        m=0
        mensaje = ""
        elementoI = '<?xml version="1"?>\n'
        elementoI2 = '<MENSAJES_RECIBIDOS>\n'
        elementoF = '</MENSAJES_RECIBIDOS>'
        for g in txtParseado.findall('MENSAJE'):
            m += 1

            for k in g.findall('FECHA'):
                fechaCompleta = k.text
            for f in g.findall('TEXTO'):
                textoM = f.text
            Hashtag, Menciones = self.analizarMensaje(textoM)
            fechaSolitaria = self.obtenerFecha(fechaCompleta)
            mensaje = '<TIEMPO>\n'
            mensaje += f'<FECHA> {fechaSolitaria} </FECHA>\n'
            mensaje += f'<MSJ_RECIBIDOS> {m} <MSJ_RECIBIDOS>\n'
            mensaje += f'<USR_MENCIONADOS> {len(Menciones)} </USR_MENCIONADOS>\n'
            mensaje += f'<HASH_INCLUIDOS> {len(Hashtag)} </HASH_INCLUIDOS>\n'
            mensaje += '</TIEMPO>\n'

        unido = elementoI + elementoI2 + mensaje + elementoF
        return unido





    def analizarMensaje(self,textoCompleto):
        Hastag = []
        mencion = []

        j = 0
        while j< len(textoCompleto):
            caracterAnalizado = textoCompleto[j]

            if caracterAnalizado == "#":
                PosFinal = textoCompleto.find('#', j + 1)
                string = textoCompleto[j + 1:PosFinal]
                j = PosFinal + 1
                print("#" + string + "#")
                Hastag.append("#" + string + "#")
            elif caracterAnalizado == "@":
                j+=1
                carI = j
                while textoCompleto[j].isalpha() or textoCompleto[j].isdigit() or textoCompleto[j] == "_":
                    j += 1
                stringMencion = textoCompleto[carI:j]
                mencion.append("@"+stringMencion)
            else:
                j+=1
        return Hastag,mencion

    def obtenerFecha(self,fecha):
        fcompleta = fecha
        i = 0
        while i < len(fcompleta):
            caracterA = fcompleta[i]
            if caracterA.isdigit() and fcompleta[i + 1].isdigit() and fcompleta[i + 2] == "/" and fcompleta[i + 3].isdigit() and fcompleta[i + 4].isdigit() and fcompleta[i + 5] == "/" and fcompleta[i + 6].isdigit() and fcompleta[i + 7].isdigit() and fcompleta[i + 8].isdigit() and fcompleta[i + 9].isdigit():
                fechaApartada = fcompleta[i:i + 10]
                i += 10
            else:
                i += 1
        return fechaApartada


    def anadirDiccionario(self,archivoDiccionario):

        InforDiccionarioCompleto = archivoDiccionario
        infoArreglada = InforDiccionarioCompleto
        listadoPalabrasPositivas = ""

        baseDatosDiccionarios = ET.parse("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml")

        print(infoArreglada)
        infoIntento = ET.fromstring(infoArreglada)
        for i in infoIntento.findall('sentimientos_positivos'):
            for j in i.findall('palabra'):
                palabraPositiva = j.text
                palabraPSinT = unidecode.unidecode(palabraPositiva)
                palabra = ET.Element("palabra")
                palabra.text = palabraPSinT
                print(palabraPositiva)
                VF = self.VerificarExistePositivos(palabraPSinT)
                VFEP = self.VerificarExisteNegativos(palabraPSinT)
                VFER = self.verificarExisteRechazdas(palabraPSinT)
                VFEOL = self.verificarExisteArchivoN(palabraPSinT,infoIntento)
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
                nP = unidecode.unidecode(palabraNegativa)
                palabra2 = ET.Element("palabra")
                palabra2.text = nP

                VF = self.VerificarExisteNegativos(nP)
                VFEN = self.VerificarExistePositivos(nP)
                VFER = self.verificarExisteRechazdas(nP)
                VFEOP = self.verificarExisteArchivoP(nP, infoIntento)
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