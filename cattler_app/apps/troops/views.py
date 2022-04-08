from rest_framework.generics import ListAPIView, CreateAPIView

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
