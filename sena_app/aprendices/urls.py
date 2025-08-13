from django.urls import path
from . import views
from .views import AprendizForm

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices, name='aprendices'),
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
    path('lista_cursos/curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('aprendices/aprendiz/<int:aprendiz_id>/', views.detalle_aprendiz, name='detalle_aprendiz'),
    path('crear_aprendiz/', AprendizForm.as_view(), name='crear_aprendiz'),
]
