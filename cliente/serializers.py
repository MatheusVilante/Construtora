from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'nome', 
            'email', 
            'telefone',
            'endereco',
            'cidade',
            'estado',
            'cep',
            'dataNascimento',
            'contratoNovo',
            'vencimento',
            'datadeAssinatura',
            'data',
            'intercalada'
            )
