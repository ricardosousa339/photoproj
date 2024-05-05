from django.http import JsonResponse
from django.shortcuts import render
from httplib2 import Response
from .forms import FotoForm
from django.http import HttpResponse
from storages.backends.gcloud import GoogleCloudStorage
from .models import Foto
from django.core.files.storage import default_storage
from django.core.files.storage import default_storage
from django.http import Http404
from rest_framework import viewsets
from .serializers import FotoSerializer
from rest_framework import viewsets
from .models import Foto
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    
    def user_photos_api(request):
        if request.method == 'GET':
            user = request.user
            photos = Foto.objects.filter(user=user)
            serializer = FotoSerializer(photos, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    ##TODO: No futuro, ao invés de associar as fotos aos usuários, associar elas a um Evento, 
    # e associar o evento ao usuário, assim fica mais separado, ao invés de todas 
    # as fotos juntas