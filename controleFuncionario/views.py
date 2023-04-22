from rest_framework import viewsets
from .models import ControleFuncionario
from .serializers import ControleFuncionarioSerializer

class ControleFuncionarioViewSet(viewsets.ModelViewSet):
    queryset = ControleFuncionario.objects.all()
    serializer_class = ControleFuncionarioSerializer