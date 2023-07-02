from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from cliente.models import Cliente
from quadraLote.models import Lote, Quadra


@permission_classes((permissions.AllowAny,))
class   ClienteApi(APIView):
    def post(self, request):
        response = Cliente.objects.all().order_by('nome').values_list('id', 'nome')
        return Response(response, status=status.HTTP_200_OK)

@permission_classes((permissions.AllowAny,))
class   QuadraApi(APIView):
    def post(self, request):
        response = Quadra.objects.all().order_by('quadra').values_list('id','residencial', 'quadra')
        return Response(response, status=status.HTTP_200_OK)

@permission_classes((permissions.AllowAny,))
class LoteApi(APIView):
    def post(self, request):
        id = request.GET.get("id")
        response = Lote.objects.filter(quadra_id=id).order_by('lote').values_list('id', 'lote')
        return Response(response, status=status.HTTP_200_OK)
