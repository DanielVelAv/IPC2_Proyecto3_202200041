import time

DiccionarioFechas={

}

DiccionarioMenciones={

}

DiccionarioFechasPuras={

}
class Hastags:
    def __init__(self,diccionario,PrimerRango,SegundoRango):
        self.diccionario = diccionario
        self.PrimerRango = PrimerRango
        self.SegundoRango = SegundoRango

    def filtar(self):

        TemporalDatos = []
        print(self.diccionario)

        primerR = time.strptime(self.PrimerRango,'%Y-%m-%d')
        segundoR = time.strptime(self.SegundoRango,'%Y-%m-%d')

        DiccionarioF = {}

        for i in range(len(self.diccionario)):
            dicc = list(self.diccionario.keys())[i]
            fechaEnDicc = self.diccionario[dicc][0]
            print(fechaEnDicc)
            fechaEnDiccTD = time.strptime(fechaEnDicc,'%d/%m/%Y')
            VerificacionRango = self.EstaEntre(primerR,segundoR,fechaEnDiccTD)
            if VerificacionRango == True:
                print(fechaEnDicc,self.diccionario[dicc][1],len(self.diccionario[dicc][1]))
                DiccionarioF[fechaEnDicc] = self.diccionario[dicc][1]


            print("diccionario Fecha:",DiccionarioF)
        return DiccionarioF
    def EstaEntre(self,RangoInicial,RangoFinal,Fecha):
        Desicion = False
        if Fecha >= RangoInicial and Fecha <= RangoFinal:
            print("En el rango Indicado")
            Desicion = True
        else:
            pass
        return Desicion


class Menciones():
    def __init__(self,diccionaro,PrimerRango,SegundoRango):
        self.diccionario = diccionaro
        self.PrimerRango = PrimerRango
        self.SegundoRango = SegundoRango

    def filtrarMenciones(self):
        primerR = time.strptime(self.PrimerRango, '%Y-%m-%d')
        segundoR = time.strptime(self.SegundoRango, '%Y-%m-%d')
        DiccionarioM = {}
        for i in range(len(self.diccionario)):
            dicc = list(self.diccionario.keys())[i]
            fechaEnDicc = self.diccionario[dicc][0]
            print(fechaEnDicc)
            fechaEnDiccTD = time.strptime(fechaEnDicc,'%d/%m/%Y')
            VerificacionRango = self.EstaEntre(primerR,segundoR,fechaEnDiccTD)
            if VerificacionRango == True:
                print(fechaEnDicc,self.diccionario[dicc][2],len(self.diccionario[dicc][2]))
                if len(self.diccionario[dicc][2]) != 0:
                    DiccionarioM[fechaEnDicc] = self.diccionario[dicc][2]
            print("diccionario Fecha:",DiccionarioM)
        return DiccionarioM
    def EstaEntre(self,RangoInicial,RangoFinal,Fecha):
        Desicion = False
        if Fecha >= RangoInicial and Fecha <= RangoFinal:
            print("En el rango Indicado")
            Desicion = True
        else:
            pass
        return Desicion

class Sentimientos():
    def __init__(self,diccionario,PrimerRango,SegundoRango):
        self.diccionario = diccionario
        self.PrimerRango = PrimerRango
        self.SegundoRango = SegundoRango

    def filtrarSentimientos(self):
        primerR = time.strptime(self.PrimerRango, '%Y-%m-%d')
        segundoR = time.strptime(self.SegundoRango, '%Y-%m-%d')
        DiccionarioSP = {}
        DiccionarioSN = {}
        for i in range(len(self.diccionario)):
            dicc = list(self.diccionario.keys())[i]
            fechaEnDicc = self.diccionario[dicc][0]
            print(fechaEnDicc)
            fechaEnDiccTD = time.strptime(fechaEnDicc, '%d/%m/%Y')
            VerificacionRango = self.EstaEntre(primerR, segundoR, fechaEnDiccTD)
            if VerificacionRango == True:
                print(fechaEnDicc, self.diccionario[dicc][2], len(self.diccionario[dicc][2]))
                DiccionarioSP[fechaEnDicc] = self.diccionario[dicc][3]
                DiccionarioSN[fechaEnDicc] = self.diccionario[dicc][4]
            print("diccionario Sentimientos:", DiccionarioSP)
        return DiccionarioSP,DiccionarioSN

    def EstaEntre(self, RangoInicial, RangoFinal, Fecha):
        Desicion = False
        if Fecha >= RangoInicial and Fecha <= RangoFinal:
            print("En el rango Indicado")
            Desicion = True
        else:
            pass
        return Desicion