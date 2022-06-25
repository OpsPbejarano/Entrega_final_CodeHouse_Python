from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    contenido = models. TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="fotos", null=True, blank=True)

    def __str__(self):
        return self.titulo
