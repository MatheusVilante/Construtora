from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from cliente.models import Cliente


@permission_classes((permissions.AllowAny,))
class   ClienteApi(APIView):
    def post(self, request):
        response = Cliente.objects.all().order_by('nome').values_list('id', 'nome')
        return Response(response, status=status.HTTP_200_OK)
