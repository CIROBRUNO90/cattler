from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView)
from rest_framework import status
from rest_framework.response import Response

from .models import lots
from .serializers import LotsSerializer

class LotsListApiView(ListAPIView):
    queryset = lots.objects.all()
    serializer_class = LotsSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')    

class LotsCreateApiView(CreateAPIView):
    """
    request:
    {
        "lot_id":1,
        "troops": [1,2]
    }  
    the troop field is optional
    """
    queryset = lots.objects.all()
    serializer_class = LotsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

class LotslDestroyApiView(DestroyAPIView):
    """
    request:
    {
        "lot_id": 1
    }
    """
    def delete(self, request, *args, **kwargs):
        lot_id = request.data.get('lot_id', None)
        msg = {"msg":'delete ok'}

        if lot_id:
            lot_del = lots.objects.filter(lot_id=lot_id).first()
            if lot_del:
                lot_del.delete()
                status_code = status.HTTP_204_NO_CONTENT
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                msg = {"error": 'Nonexistent lot'}
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = {"error":'lot id required'}

        return Response(status=status_code, data=msg)    