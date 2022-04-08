from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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
