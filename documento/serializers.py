from rest_framework import serializers
from .models import Documento, Historico

class DocumentoReadSerializer(serializers.ModelSerializer):
    lote = serializers.ReadOnlyField(source='lote.lote')
    class Meta:
        model = Documento
        fields = ['id', 'lote', 'tipo_documento', 'data', 'situacao']

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ['id', 'lote', 'tipo_documento', 'data', 'situacao']

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['id', 'descricao', 'data','lote']