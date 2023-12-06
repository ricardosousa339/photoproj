from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos/')