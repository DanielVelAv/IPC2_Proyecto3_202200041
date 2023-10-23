from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
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

@ensure_csrf_cookie
def pedirEntrada(request):
    context = RequestContext(request)
    if request.method == 'POST':
        archivoMensajes = request.POST['archivoE']
        messages.success(request,"Se ha enviado correctamente el archivo")
        return HttpResponse('Archivo REcibido')
    objetoTemplate = loader.get_template("Principal.html")
    html = objetoTemplate.render({})
    return HttpResponse(html)