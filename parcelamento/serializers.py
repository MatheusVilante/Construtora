from rest_framework import serializers
from .models import Parcelamento

class ParcelamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelamento
        fields = '__all__'
