from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from cms.barrapunto import obtener_noticias
# Create your views here.

def pagina(request, identificador):
    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
        noticias = obtener_noticias()
        respuesta += "<h1>Las noticias de barrapunto son: </h1>" + noticias
    except Pages.DoesNotExist:
        respuesta = "No existe en la base de datos"
    return HttpResponse(respuesta)
def mostrar(resquest):
    lista=Pages.objects.all()
    respuesta ="<ol>"
    for pag in lista:
        respuesta +='<li><a href="' + str(pag.id) +'">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
