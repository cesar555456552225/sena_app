from django.urls import path
from . import views

app_name='instructor'

urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
]