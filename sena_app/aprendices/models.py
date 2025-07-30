from django.db import models


# Create your models here.

class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=225)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=155)
    programa = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"
    def nombre_aprendiz(self):
        return f"{self.nombres} {self.apellido}"

