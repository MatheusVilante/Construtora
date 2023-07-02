from django.urls import path

from dropbox.views import ClienteApi, LoteApi, QuadraApi

urlpatterns = [
    path('api/v1/select/cliente', ClienteApi.as_view(), name='select'),
    path('api/v1/select/quadra', QuadraApi.as_view(), name='select'),
    path('api/v1/select/lote', LoteApi.as_view(), name='select'),
]