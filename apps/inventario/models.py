from django.db import models

# Create your models here.
class Estudiante(models.Model):
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Computadora(models.Model):
    numero = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca}, {self.numero}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"
    
class Prestamo(models.Model):
    fecha_retiro = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True)
    devolucion = models.BooleanField(null=True)
    motivo = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estudiante}, {self.fecha_retiro}"