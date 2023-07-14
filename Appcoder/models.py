from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    def __str__(self):
        return f"nombre: {self.nombre} - camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()    
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} email: {self.email} profesion{self.profesion}"

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregada = models.BooleanField() 
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='avatares', null = True, blank = True)   

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    author_name = models.CharField(max_length=100, default='')
    subtitle = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']    