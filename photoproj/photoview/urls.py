from django.urls import path
from . import views
from .views import galeria

urlpatterns = [
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('galeria/', views.galeria, name = "Galeria"),
]
