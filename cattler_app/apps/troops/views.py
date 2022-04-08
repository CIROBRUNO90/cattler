from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView)
from rest_framework import status
from rest_framework.response import Response

from .models import troop
from .serializers import TroopSerializer


class TroopListApiView(ListAPIView):
    """
    request:
    {
        "lot_id": 1
    }    
    """
    queryset = troop.objects.all()
    serializer_class = TroopSerializer

    def get_queryset(self):
        lot_id = self.request.data.get('lot_id')
        if lot_id:
            return self.queryset.filter(lots__lot_id=lot_id).order_by('id')
        return self.queryset.order_by('id')        

class TroopCreateApiView(CreateAPIView):
    """
    request:
    {
        "troop_id": 4
    }    
    """
    queryset = troop.objects.all()
    serializer_class = TroopSerializer

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class TroopDestroyApiView(DestroyAPIView):
    """
    request:
    {
        "troop_id": 1
    }
    """
    def delete(self, request, *args, **kwargs):
        troop_id = request.data.get('troop_id', None)
        msg = {"msg":'delete ok'}

        if troop_id:
            troop_del = troop.objects.filter(troop_id=troop_id).first()
            if troop_del:
                troop_del.delete()
                status_code = status.HTTP_204_NO_CONTENT
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                msg = {"error": 'Nonexistent troop'}
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = {"error":'troop id required'}

        return Response(status=status_code, data=msg)