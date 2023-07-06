from rest_framework import viewsets
from .models import Documento, Historico
from .serializers import DocumentoSerializer, HistoricoSerializer, DocumentoReadSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DocumentoReadSerializer
        return DocumentoSerializer

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer