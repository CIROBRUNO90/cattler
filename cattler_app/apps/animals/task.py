
from django.db import transaction

from .models import animals
from apps.corrals.models import corral
from apps.lots.models import lots
from apps.troops.models import troop

@transaction.atomic
def animals_ingress(data):
    msg = {"msg":'ingress OK'}
    err_cod = 0
    last_troop = 0
    lot_id = data.get('lot_id')
    ingress = data.get('ingress')
    lot_ing = lots.objects.filter(lot_id=lot_id).first()

    if lot_ing:
        for item in ingress:
            if not corral.objects.filter(corral_id=item.get('corral')).exists():
                if troop.objects.last():
                    last_troop = troop.objects.last().troop_id

                troop_ing = troop.objects.create(troop_id=(last_troop+1))
                corral_ing = corral.objects.create(
                    corral_id=item.get('corral'),
                    troop=troop_ing)
                cant_animals = item.get('quantity')
                
                for i in range(cant_animals-1):
                    animal_ing = animals.objects.create(troop=troop_ing)
                lot_ing.troops.add(troop_ing)
            else:
                err_cod = 2
                msg = {"error":'Existing corral'}
                break
    else:
        err_cod = 1
        msg = {"error":'Nonexistent lot'}
    
    return msg, err_cod