from rest_framework import viewsets
from .models import Devolucao, DevolucaoParcela
from .serializers import DevolucaoSerializer, DevolucaoParcelaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class DevolucaoViewSet(viewsets.ModelViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_destroy(self, instance):
        instance.delete()

class DevolucaoParcelaViewSet(viewsets.ModelViewSet):
    queryset = DevolucaoParcela.objects.all()
    serializer_class = DevolucaoParcelaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_destroy(self, instance):
        instance.delete()
