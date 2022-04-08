from django.db import models

from apps.troops.models import troop


class animals(models.Model):
    caravana = models.IntegerField(unique=True, null=True)
    rfid = models.IntegerField(null=True)
    troop = models.ForeignKey(troop, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.caravana) + '-' + str(self.rfid)