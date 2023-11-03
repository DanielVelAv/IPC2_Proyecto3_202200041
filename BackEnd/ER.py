import xml.etree.ElementTree as ET
from collections import namedtuple
import re

Mensaje = namedtuple('Mensaje','Mensaje')
Fecha = namedtuple('Fecha',"Date")
Texto = namedtuple('Texto','text')

Twitter = {

}

Diccionario = {

}

class ER():
    def __init__(self):
        self.raiz = ET.parse("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/db.xml").getroot()
        self.raizDiccionario = ET.parse("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/dbDiccionario.xml").getroot()

    def getDatos(self):
        fecha = None
        texto = None

        for h in self.raizDiccionario.findall('sentimientos_negativos'):
            for g in h.findall('palabra'):
                print(g.text)
                SinE = g.text.strip()
                Sinupper = SinE.lower()
                Diccionario[Sinupper] = 'Negativo'

        for o in self.raizDiccionario.findall('sentimientos_positivos'):
            for y in o.findall('palabra'):
                sinEs = y.text.strip()
                SinUpp = sinEs.lower()
                Diccionario[SinUpp] = 'Positivo'


        print(Diccionario)

        m = 0

        for i in self.raiz.findall('MENSAJE'):
            m += 1
            for j in i.findall('FECHA'):
                fechasCompletas = j.text
                fecha = fechasCompletas
            for k in i.findall('TEXTO'):
                textoBD = k.text
                texto = textoBD
            Hashtag, Menciones, PPositivas,PNegativas = self.analizarMensaje(textoBD)
            FechaSolitaria = self.obtenerFecha(fechasCompletas)
            print("-Fecha-",FechaSolitaria,"-Hashtags-",Hashtag,"-Menciones-",Menciones,"-Positivas-",PPositivas,"-Negativas-",PNegativas)
            Twitter[m] = [FechaSolitaria,Hashtag,Menciones,PPositivas,PNegativas]

        return Twitter


    def analizarMensaje(self,txtCompleto):

        Hashtag = []
        Mencion = []
        Negativos = 0
        Positivos = 0
        Neutros = 0

        j = 0
        while j<len(txtCompleto):

            caracterAnalizado = txtCompleto[j]

            if caracterAnalizado == "#":
                PosFinal = txtCompleto.find('#',j+1)
                string = txtCompleto[j+1:PosFinal]
                j = PosFinal + 1
                print("#"+string+"#")
                Hashtag.append("#" + string + "#")
            elif caracterAnalizado == "@":
                j+=1
                carI = j
                while txtCompleto[j].isalpha() or txtCompleto[j].isdigit() or txtCompleto[j] == "_":
                    j += 1
                StringMencion = txtCompleto[carI:j]
                print("@"+StringMencion)
                Mencion.append("@"+StringMencion)
            elif caracterAnalizado.isalpha():
                k = j
                while k < len(txtCompleto) and txtCompleto[k].isalpha():
                    k += 1
                string = txtCompleto[j:k]
                print(string)
                StringSinM = string.lower()
                if StringSinM in Diccionario:
                    print("Se encuentra")
                    if Diccionario[StringSinM] == "Negativo":
                        Negativos += 1
                    elif Diccionario[StringSinM] == "Positivo":
                        Positivos += 1
                    print("negativos: ", Negativos, " Positivos: ", Positivos)
                else:
                    print("Nope")
                j = k
            else:
                j+=1

        return Hashtag,Mencion,Positivos,Negativos

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