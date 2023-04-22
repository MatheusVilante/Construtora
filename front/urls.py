from django.conf.urls import url
from django.urls import path

from .views import clienteLote, index, cliente, lote, quadra


urlpatterns = [
    path('index', index, name='index'),
    path('cliente', cliente, name='cliente'),
    path('quadra', quadra, name='quadra'),
    path('lote', lote, name='lote'),
    path('clienteLote', clienteLote, name='clienteLote'),
]