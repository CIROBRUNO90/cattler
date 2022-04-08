from django.urls import path

from .views import (
    TroopListApiView,
    TroopCreateApiView,
    TroopDestroyApiView
    )

app_name='troops_app'

urlpatterns = [
    path(
        'troops-list/',
        TroopListApiView.as_view(),
        name='troop_list'),
    path(
        'troop-create/',
        TroopCreateApiView.as_view(),
        name='troop_create'),        
    path(
        'troop-delete/',
        TroopDestroyApiView.as_view(),
        name='troop_delete'),                
]