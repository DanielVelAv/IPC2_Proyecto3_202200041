import xml.etree.ElementTree as ET
from collections import namedtuple
import re

Mensaje = namedtuple('Mensaje','Mensaje')
Fecha = namedtuple('Fecha',"Date")
Texto = namedtuple('Texto','text')

Twitter = {

}

class ER():
    def __init__(self):
        self.raiz = ET.parse("C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto3_202200041/BackEnd/db.xml").getroot()

    def getDatos(self):
        fecha = None
        texto = None

        i = 0

        for i in self.raiz.findall('MENSAJE'):
            for j in i.findall('FECHA'):
                fechasCompletas = j.text
                fecha = fechasCompletas
            for k in i.findall('TEXTO'):
                textoBD = k.text
                texto = textoBD
            self.analizarMensaje(textoBD)
            self.obtenerFecha(fechasCompletas)

        return fecha,texto

    def analizarMensaje(self,txtCompleto):

        Hashtag = None
        Mencion = None


        j = 0
        while j<len(txtCompleto):

            caracterAnalizado = txtCompleto[j]

            if caracterAnalizado == "#":
                PosFinal = txtCompleto.find('#',j+1)
                string = txtCompleto[j+1:PosFinal]
                j = PosFinal + 1
                print("#"+string+"#")
            elif caracterAnalizado == "@":
                j+=1
                carI = j
                while txtCompleto[j].isalpha() or txtCompleto[j].isdigit() or txtCompleto[j] == "_":
                    j += 1
                StringMencion = txtCompleto[carI:j]
                print("@"+StringMencion)
            else:
                j+=1

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