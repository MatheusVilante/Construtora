from rest_framework import serializers

from quadraLote.models import Lote
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
        
class LeituraDespesaSerializer(serializers.ModelSerializer):
    lote = serializers.ReadOnlyField(source='lote.lote')
    quadra = serializers.ReadOnlyField(source='lote.quadra.quadra')

    class Meta:         
        model = Despesa
        fields = (
            'id',
            'valor',
            'data',
            'lote',
            'devolucao',
            'quadra',
            'situacao',
        )
