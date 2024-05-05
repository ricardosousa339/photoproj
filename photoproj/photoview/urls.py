from django.urls import path, include
from . import views
from . import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('galeria/', views.galeria, name = "Galeria"),
    path('api/photo/user_photos/', viewsets.PhotoViewSet.user_photos_api, name='user-photos-api'),
    path('', include(router.urls)),
]
