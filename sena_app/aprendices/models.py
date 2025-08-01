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
    


class curso(models.Model):
    ESTADO_CHOICES = [
        ('PRO', 'Programado'),
        ('INI', 'Iniciado'),
        ('EJE', 'Ejecución'),
        ('FIN', 'Finalizado'),
        ('CAN', 'Cancelado'),
        ('SUS', 'Suspendido'),
    ]

    codigo = models.CharField(max_length=30,unique=True,verbose_name="Codiogo",)
    nombre = models.CharField(max_length=200,verbose_name="Nombre del curso")
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, verbose_name='Programa de formación')
    instructor_coordinador = models.ForeignKey('instructores.Instructor',on_delete=models.CASCADE,related_name='cursos_coordinador',verbose_name="Instructor coordinador")
    instructores = models.ManyToManyField('instructores.Instructor',through='InstructorCurso', related_name='cursos_impartidos', verbose_name='Instructores')
    aprendices = models.ManyToManyField(Aprendiz,through='AprendizCurso',related_name='cursos',verbose_name='Aprendices')
    fecha_inicio= models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    horario = models.CharField(max_length=100, verbose_name="Horario")
    aula = models.CharField(max_length=50, verbose_name="Aula/Ambiente")
    cupos_maximos = models.PositiveBigIntegerField(verbose_name="Cupos Maximos")
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PRO', verbose_name="Estado del curso")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")
