
from rest_framework import serializers

from .models import animals

class AnimalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = animals
        fields = ['caravana', 'rfid', 'troop']

    def create(self, validated_data):
        return super().create(validated_data)