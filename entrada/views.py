from rest_framework import viewsets
from .models import Entrada
from .serializers import EntradaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_destroy(self, instance):
        instance.delete()