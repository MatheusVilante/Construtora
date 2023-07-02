from rest_framework import serializers
from .models import Quadra, Lote
from cliente.serializers import ClienteSerializer

class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'


class FluxoSerializer(serializers.ModelSerializer):
    quadra = serializers.ReadOnlyField(source='quadra.quadra')
    residencial = serializers.ReadOnlyField(source='quadra.residencial')
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    cpf = serializers.ReadOnlyField(source='cliente.cpf')

    class Meta:         
        model = Lote
        fields = (
            'id',
            'codigo_de_contrato',
            'residencial',
            'quadra',
            'lote',
            'data_de_habita',
            'cliente',
            'cpf',
            'data_de_venda',
            'valor_de_venda',
            'taxa_de_juros',
            'indexador_ate_habitase',
        )
