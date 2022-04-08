from rest_framework import serializers

from .models import corral

class CorralSerializer(serializers.ModelSerializer):

    class Meta:
        model = corral
        fields = ['corral_id', 'troop']

    def create(self, validated_data):
        return super().create(validated_data)