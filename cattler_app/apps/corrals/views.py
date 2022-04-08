from rest_framework.generics import ListAPIView, CreateAPIView
# Create your views here.
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