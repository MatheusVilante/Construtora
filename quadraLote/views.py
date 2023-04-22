from rest_framework import viewsets
from .models import Quadra, Lote
from .serializers import QuadraSerializer, LoteSerializer

class QuadraViewSet(viewsets.ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer


class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer