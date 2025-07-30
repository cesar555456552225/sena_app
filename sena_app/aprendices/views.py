from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all()
    template = loader.get_template('aprendiz.html')
    context ={
        'aprendices' : lista_aprendices,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())