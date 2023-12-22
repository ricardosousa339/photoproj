from rest_framework.routers import SimpleRouter
from photoview.user.viewsets import UserViewSet
from photoview.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from photoview.views import PhotoViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

routes.register(r'photo', PhotoViewSet, basename='photo')

urlpatterns = [
    *routes.urls
]