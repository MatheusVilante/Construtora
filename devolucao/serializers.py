from rest_framework import serializers
from .models import Devolucao, DevolucaoParcela

class DevolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucao
        fields = ['id', 'lote_id', 'data_restituicao', 'valor_restituir', 'parcelamento', 'parcela']


class DevolucaoParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevolucaoParcela
        fields = ('id', 'devolucao_id', 'valor', 'data_referencia', 'data_pagamento', 'excluido', 'data_exclusao')
        read_only_fields = ('id', 'excluido', 'data_exclusao')