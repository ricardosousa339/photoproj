from django.db import models
from django.utils import timezone

from photoproj import settings

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.titulo:
            self.titulo = 'Foto ' + timezone.now().strftime('%Y%m%d-%H%M%S')
        super().save(*args, **kwargs)