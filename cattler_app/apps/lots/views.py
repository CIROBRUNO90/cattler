from rest_framework.generics import ListAPIView, CreateAPIView

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