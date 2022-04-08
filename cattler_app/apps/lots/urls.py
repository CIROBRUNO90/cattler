from django.urls import path

from .views import (
    LotsListApiView,
    LotsCreateApiView,
    LotslDestroyApiView
    )

app_name='lots_app'

urlpatterns = [
    path(
        'lots-list/',
        LotsListApiView.as_view(),
        name='lots_list'),
    path(
        'lot-create/',
        LotsCreateApiView.as_view(),
        name='lot_create'),        
    path(
        'lot-delete/',
        LotslDestroyApiView.as_view(),
        name='lot_delete'),                
]