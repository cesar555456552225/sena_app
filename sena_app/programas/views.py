from django.shortcuts import render
from django.template import loader
from .models import Programa
from django.http import HttpResponse
# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('programas.html')
    context ={
        'programas' : lista_programas,
    }
    return HttpResponse(template.render(context, request))

def main (request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render)