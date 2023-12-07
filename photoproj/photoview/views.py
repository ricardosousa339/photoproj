from django.http import JsonResponse
from django.shortcuts import render
from .forms import FotoForm
from .models import Foto
from django.core.files.storage import default_storage
from rest_framework import viewsets
from .serializers import FotoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token


def upload_imagem(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirecione ou processe conforme necessário
    else:
        form = FotoForm()
    return render(request, 'photoview/upload.html', {'form': form})


def galeria(request):
    fotos = Foto.objects.all()
    context = {
        'fotos': []
    }

    for foto in fotos:
        try:
            # Tenta obter a URL do objeto, mas verifica se o objeto existe
            imagem_url = default_storage.url(foto.imagem.name)
            context['fotos'].append({
                'titulo': foto.titulo,
                'imagem_url': imagem_url
            })
        except FileNotFoundError:
            # Se o arquivo não for encontrado, a imagem foi excluída
            print(f"A imagem para a foto com o título '{foto.titulo}' não foi encontrada.")
            # Opcional: Marque a foto para exclusão do banco de dados, se desejar
            foto.delete()

    response = render(request, 'photoview/galeria.html', context)
    response['Cache-Control'] = 'public, max-age=86400'
    del response['Expires']

    return response


#### API

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@ensure_csrf_cookie
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
