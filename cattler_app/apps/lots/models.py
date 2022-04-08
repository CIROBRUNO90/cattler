from django.db import models

from apps.troops.models import troop

class lots(models.Model):
    lot_id = models.IntegerField(unique=True)
    troops = models.ManyToManyField(troop, default=None)

    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.lot_id)