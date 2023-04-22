from rest_framework import serializers
from .models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ['id', 'lote', 'cliente', 'tipo_documento', 'situacao']