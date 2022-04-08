from django.urls import path

from .views import (
    AnimalsListView,
    AnimalsCreateApiView,
    AnimalsIngressApiView,
    AnimalsDestroyApiView
    )

app_name='animals_app'

urlpatterns = [
    path(
        'animals-list/',
        AnimalsListView.as_view(),
        name='animals_list'),
    path(
        'animals-create/',
        AnimalsCreateApiView.as_view(),
        name='animals_create'),       
    path(
        'animals-delete/',
        AnimalsDestroyApiView.as_view(),
        name='animals_delete'),                
    path(
        'animals-ingress/',
        AnimalsIngressApiView.as_view(),
        name='animals_ingress'),        
]