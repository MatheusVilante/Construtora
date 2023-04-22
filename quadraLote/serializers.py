from rest_framework import serializers
from .models import Quadra, Lote
from cliente.serializers import ClienteSerializer

class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Lote
        fields = '__all__'