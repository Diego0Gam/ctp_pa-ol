from django.contrib import admin
from .models import Estudiante, Computadora, Prestamo, Curso, Materia

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Computadora)
admin.site.register(Prestamo)
admin.site.register(Curso)
admin.site.register(Materia)