from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    unique_together = ('nome', 'cpf')	
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nome', 
            'email',
            'cpf',
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
            'intercalada',
            'profissao',
            'rg',
            )
