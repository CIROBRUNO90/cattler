from django.db import models

from apps.troops.models import troop

class corral(models.Model):
    corral_id = models.IntegerField(unique=True)
    troop = models.ForeignKey(troop, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.corral_id)