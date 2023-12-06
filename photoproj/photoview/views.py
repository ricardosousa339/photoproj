from django.shortcuts import render
from .forms import FotoForm
from django.http import HttpResponse
from storages.backends.gcloud import GoogleCloudStorage
from .models import Foto
from django.core.files.storage import default_storage
from django.core.files.storage import default_storage
from django.http import Http404

def upload_imagem(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirecione ou processe conforme necessário
    else:
        form = FotoForm()
    return render(request, 'photoview/upload.html', {'form': form})

def serve_image(request, file_name):
    storage = GoogleCloudStorage()
    image_file = storage.open('fotos/' + file_name, 'rb')
    return HttpResponse(image_file, content_type='image/jpeg')


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

    return render(request, 'photoview/galeria.html', context)

