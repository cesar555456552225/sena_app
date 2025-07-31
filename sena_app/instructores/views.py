from django.shortcuts import render
from django.template import loader
from .models import Instructor
from django.http import HttpResponse
# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template('instructor.html')
    context={
        'instructores' : lista_instructores,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())