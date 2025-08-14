from django.urls import path
from . import views
from .views import InstructorFormView

app_name='instructor'

urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
    path('crear_instructor/', InstructorFormView.as_view(), name='crear_instructor'),
]