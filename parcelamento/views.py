from rest_framework import viewsets
from .models import Parcelamento
from .serializers import ParcelamentoSerializer

class ParcelamentoViewSet(viewsets.ModelViewSet):
    queryset = Parcelamento.objects.all()
    serializer_class = ParcelamentoSerializer
