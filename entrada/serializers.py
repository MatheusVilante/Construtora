from rest_framework import serializers
from .models import Entrada

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '_all_'
        read_only_fields = ('id', 'excluido', 'data_exclusao')