from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView)
from rest_framework import status
from rest_framework.response import Response

from .models import corral
from .serializers import CorralSerializer

class CorralListApiView(ListAPIView):
    queryset = corral.objects.all()
    serializer_class = CorralSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')

class CorralCreateApiView(CreateAPIView):
    """
    request:
    {
        "corral_id": 111,
        "troop": 1
    }    
    """
    queryset = corral.objects.all()
    serializer_class = CorralSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CorralDestroyApiView(DestroyAPIView):
    """
    request:
    {
        "corral_id": 1
    }
    """
    def delete(self, request, *args, **kwargs):
        corral_id = request.data.get('corral_id', None)
        msg = {"msg":'delete ok'}

        if corral_id:
            corral_del = corral.objects.filter(corral_id=corral_id).first()
            if corral_del:
                corral_del.delete()
                status_code = status.HTTP_204_NO_CONTENT
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                msg = {"error": 'Nonexistent corral'}
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = {"error":'corral id required'} 

        return Response(status=status_code, data=msg)    