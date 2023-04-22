from rest_framework import serializers
from .models import ControleCheque

class ControleChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleCheque
        fields = '__all__'