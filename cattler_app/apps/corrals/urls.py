from django.urls import path

from .views import CorralCreateApiView, CorralListApiView

app_name='corrals_app'

urlpatterns = [
    path(
        'corrals-list/',
        CorralListApiView.as_view(),
        name='corral_list'),
    path(
        'corrals-create/',
        CorralCreateApiView.as_view(),
        name='corrals_create'),        
]