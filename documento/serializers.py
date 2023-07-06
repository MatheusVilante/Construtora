from rest_framework import serializers
from .models import Documento, Historico

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ['id', 'lote', 'cliente', 'tipo_documento', 'data', 'situacao']
class DocumentoReadSerializer(serializers.ModelSerializer):
    lote = 
    class Meta:
        model = Documento
        fields = ['id', 'lote', 'cliente', 'tipo_documento', 'data', 'situacao']

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['id', 'descricao', 'data','lote']