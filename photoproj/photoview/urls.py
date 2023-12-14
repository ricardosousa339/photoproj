from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('galeria/', views.galeria, name = "Galeria"),
    path('', include(router.urls)),
]
