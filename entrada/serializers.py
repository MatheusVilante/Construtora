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
