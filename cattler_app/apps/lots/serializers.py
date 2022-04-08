from rest_framework import serializers

from .models import lots

class LotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = lots
        fields = ['lot_id', 'troops']

    def create(self, validated_data):
        return super().create(validated_data)