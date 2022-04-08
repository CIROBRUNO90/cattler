from django.db import models


class troop(models.Model):
    troop_id = models.IntegerField(unique=True, null=False)

    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.troop_id)