from rest_framework import serializers

from .utils import extract_main_color
from .models import Foto
from .user.models import User

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ['id','titulo', 'imagem', 'user', 'main_color']

    def create(self, validated_data):
        email = validated_data.pop('user')
        user = User.objects.get(email=email)

        
        image = validated_data.get('imagem')
        main_color = extract_main_color(image)

        return Foto.objects.create(user=user, main_color=main_color, **validated_data)