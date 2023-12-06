from django.db import models
from django.utils import timezone

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos/')

    def save(self, *args, **kwargs):
        if not self.titulo:
            self.titulo = 'Foto ' + timezone.now().strftime('%Y%m%d-%H%M%S')
        super().save(*args, **kwargs)