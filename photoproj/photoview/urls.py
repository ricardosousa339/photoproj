from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import FotoViewSet

router = DefaultRouter()
router.register(r'foto', FotoViewSet)

urlpatterns = [
    path('getCSRFToken', csrf),
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('galeria/', views.galeria, name = "Galeria"),
    path('', include(router.urls)),
]
