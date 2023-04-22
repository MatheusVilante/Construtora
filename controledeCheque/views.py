from rest_framework import viewsets
from .models import ControleCheque
from .serializers import ControleChequeSerializer


class ControleChequeViewSet(viewsets.ModelViewSet):
    queryset = ControleCheque.objects.all()
    serializer_class = ControleChequeSerializer