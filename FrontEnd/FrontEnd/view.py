from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from requests import post, get
from django.contrib import messages


def idk(request):

    url = "http://127.0.0.1:5000/"

    response = get(url)
    '''print(response.json())'''

    objetoTemplate = loader.get_template("Principal.html")
    html = objetoTemplate.render({})
    return HttpResponse(html)

@csrf_exempt
def pedirEntrada(request):
    #siempre debe tener url (post,get), debe ser igual a la de backed /point
    url = "http://127.0.0.1:7000/entradaMensaje"

    if request.method == 'POST':
        #obtendra el archivo del request (id)
        archivoMensajes = request.FILES['archivoMsg']
        #lee las forms con diccionario (flask)
        diccionarioPrueba = {'archivoMsg':archivoMensajes.read().decode('utf-8')}
        #derecho se hace un apeticion de forma de post, la direccion a donde sera y lo que le mandas, la variable es la respuesta que da del backend
        respuesta = post(url,diccionarioPrueba)
        dicc2 = {'fireworks': respuesta.content.decode()}
        objetoTemplate = loader.get_template("Principal.html")
        #respuesta va a modificar el template
        html = objetoTemplate.render(dicc2)
        return HttpResponse(html)
    objetoTemplate = loader.get_template("Principal.html")
    html = objetoTemplate.render({})
    return HttpResponse(html)

@csrf_exempt
def pedirDiccionario(request):

    url = "http://127.0.0.1:7000/CargaArchivosConfiguracion"

    if request.method == "POST":
        archivoDiccionario = request.FILES['archivoDicc']
        dicc = {'archivoDicc': archivoDiccionario.read().decode('utf-8')}
        response = post(url,dicc).json()
        '''dicc2 = {'fireworks': response.content}'''
        objectTemplate = loader.get_template("EnviarDiccionarios.html")
        html = objectTemplate.render(response)
        return HttpResponse(html)
    objetoTemplate = loader.get_template("EnviarDiccionarios.html")
    html = objetoTemplate.render({})
    return HttpResponse(html)
@csrf_exempt
def resetearDatos(request):
    url = "http://127.0.0.1:7000/LimpiarDatos"

    if request.method == "POST":
        pass
@csrf_exempt
def consultarHashtags(request):

    url = "http://127.0.0.1:7000/devolverHastags"

    if request.method == "POST":
        diccionarioAuxiliar = request.POST.dict()
        respuesta = post(url,diccionarioAuxiliar).json()
        diccpick = {'fechas':respuesta}
        objetoTemplate = loader.get_template("RecibeHashtags.html")
        html = objetoTemplate.render(diccpick)
        return HttpResponse(html)
    if request.method == "GET":
        objetoTemplate = loader.get_template("DevolverHashtags.html")
        html = objetoTemplate.render()
        return HttpResponse(html)

@csrf_exempt
def consultarMenciones(request):
    url = "http://127.0.0.1:7000/devolverMenciones"

    if request.method == "POST":
        diccionarioAuxiliar = request.POST.dict()
        respuesta = post(url,diccionarioAuxiliar).json()
        diccionario = {'fechas':respuesta}
        objetoT = loader.get_template("RecibeMenciones.html")
        html = objetoT.render(diccionario)
        return HttpResponse(html)
    if request.method == "GET":
        objetoT = loader.get_template("ConsultarMenciones.html")
        html = objetoT.render()
        return HttpResponse(html)

@csrf_exempt
def consultarSentimientos(request):
    url = "http://127.0.0.1:7000/devolverSentimientos"

    if request.method == "POST":
        diccionarioAuxiliar = request.POST.dict()
        respuesta = post(url, diccionarioAuxiliar).json()
        diccionario = {'SentP': respuesta}
        objetoT = loader.get_template("RecibeSentimientos.html")
        html = objetoT.render(diccionario)
        return HttpResponse(html)
    if request.method == "GET":
        objetoT = loader.get_template("ConsultarSentimientos.html")
        html = objetoT.render()
        return HttpResponse(html)

@csrf_exempt
def ayuda(request):
    objetoTemplate = loader.get_template("ayuda.html")
    html = objetoTemplate.render()
    return HttpResponse(html)