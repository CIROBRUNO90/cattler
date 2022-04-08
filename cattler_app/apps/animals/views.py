from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Q

from .models import animals
from .serializers import AnimalsSerializer
from .task import animals_ingress

class AnimalsListView(ListAPIView):
    """
    request:
    {
        "troop":1
    }    
    """
    queryset = animals.objects.all()
    serializer_class = AnimalsSerializer

    def get_queryset(self):
        troop_id = self.request.data.get('troop')
        if troop_id:
            return self.queryset.filter(
                troop_id=troop_id
            ).order_by('id')

        return self.queryset.order_by('id')            

class AnimalsCreateApiView(CreateAPIView):
    """
    request:
    {
        "caravana": 1,
        "rfid": 321,
        "troop": 4
    }    
    """
    queryset = animals.objects.all()
    serializer_class = AnimalsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AnimalsDestroyApiView(DestroyAPIView):
    """
    request:
    {
        "caravana": 1,
        "rfid": 321,
    }        
    """
    def delete(self, request, *args, **kwargs):
        caravana = request.data.get('caravana', None)
        rfid = request.data.get('rfid', None)
        msg = {"msg":'delete ok'}

        if caravana or rfid:
            animal_del = animals.objects.filter(Q(caravana=caravana) | Q(rfid=rfid))
            if animal_del:
                animal_del.delete()
                status_code = status.HTTP_204_NO_CONTENT
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                msg = {"error": 'Nonexistent animal'}    
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = {"error":'caravana or rfid required'}

        return Response(status=status_code, data=msg)

class AnimalsIngressApiView(APIView):
    """
    request:
    {
        "lot_id":12,
        "ingress":[
            {
                "corral": 2,
                "quantity": 5
            }
        ]
    }    
    """
    def post(self, request):
        msg, err_code = animals_ingress(request.data)

        if err_code:
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            status_code = status.HTTP_201_CREATED

        return Response(
            status=status_code,
            data=msg)
