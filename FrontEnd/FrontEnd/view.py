from django.http import HttpResponse
from django.template import loader
from requests import post, get


def idk(request):

    objetoTemplate = loader.get_template("Principal.html")
    html = objetoTemplate.render({})
    return HttpResponse(html)
