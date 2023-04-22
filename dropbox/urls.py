from django.urls import path

from dropbox.views import ClienteApi

urlpatterns = [
    path('api/v1/select/cliente', ClienteApi.as_view(), name='select'),
]