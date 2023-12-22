from rest_framework import serializers
from .models import Foto
from .user.models import User

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ['titulo', 'imagem', 'user']

    def create(self, validated_data):
        email = validated_data.pop('user')
        user = User.objects.get(email=email)
        return Foto.objects.create(user=user, **validated_data)
