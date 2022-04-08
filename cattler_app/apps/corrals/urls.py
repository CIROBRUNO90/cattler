from django.urls import path

from .views import (
    CorralCreateApiView,
    CorralListApiView,
    CorralDestroyApiView)

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
    path(
        'corrals-delete/',
        CorralDestroyApiView.as_view(),
        name='corrals_delete'),                
]