from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from aplicacion_familiares.models import Familiares

def probar_template(request):
    queryset = Familiares.objects.all()
    diccionario = {'Familiares': queryset}
    plantilla=loader.get_template('familiares_lista.html')
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)
    
