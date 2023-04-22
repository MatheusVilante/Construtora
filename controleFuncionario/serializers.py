from rest_framework import serializers
from .models import ControleFuncionario

class ControleFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleFuncionario
        fields = ['id', 'funcionario', 'dias', 'total', 'periodo']
