from rest_framework import serializers

from .models import troop

class TroopSerializer(serializers.ModelSerializer):

    class Meta:
        model = troop
        fields = ['troop_id']

    def create(self, validated_data):
        return super().create(validated_data)