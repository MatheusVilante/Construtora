from rest_framework import serializers
from .models import Entrada

class EntradaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Entrada
        fields = (
            'id',
            'observacoes',
            'lote',
            'cliente',
            'situacao',
            'vencimento',
            'valor_pago',
            'valor_a_receber',
            'numero_boleto_empresa',
            'numero_boleto_cliente',
            'parcela',
        )


class EntradaREADSerializer(serializers.ModelSerializer):
    lote = serializers.CharField(read_only=True, source='lote.lote')
    quadra = serializers.CharField(read_only=True, source='lote.quadra')
    class Meta:
        model = Entrada
        fields = (
            'id',
            'observacoes',
            'lote',
            'quadra',
            'cliente',
            'situacao',
            'vencimento',
            'valor_pago',
            'valor_a_receber',
            'numero_boleto_empresa',
            'numero_boleto_cliente',
            'parcela',
        )
