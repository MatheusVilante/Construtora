from rest_framework import viewsets
from decimal import Decimal
from entrada.models import Entrada
from .models import Quadra, Lote
from .serializers import FluxoSerializer, LoteReadSerializer, QuadraSerializer, LoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Prefetch
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class QuadraViewSet(viewsets.ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LoteReadSerializer
        return LoteSerializer

class FluxoViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = FluxoSerializer
    
    
class ClienteLoteView(APIView):
    def get(self, request):
        id = request.GET.get("id")
        parametro = Lote.objects.filter(cliente_id=id)
        serializer_class = LoteReadSerializer(parametro, many=True)
        return Response(serializer_class.data)
    
    
class Disponibilidade(APIView):
    def get(self, request):
        # Consulte as quadras com prefetch dos lotes
        quadras = Quadra.objects.prefetch_related('QuadraLote')

        # Crie a estrutura de dados para retornar na API
        estoque = []
        for quadra in quadras:
            quadra_data = {
                'fileira': quadra.quadra,
                'lotes': []
            }
            for lote in quadra.QuadraLote.all():
                lote_data = {
                    'lote': lote.lote,
                    'disponibilidade': lote.disponibilidade
                }
                quadra_data['lotes'].append(lote_data)
            estoque.append(quadra_data)

        # Retorne os dados como uma resposta JSON
        return JsonResponse(estoque, safe=False)
    
class ProjecaoParcelasView(APIView):
    def post(self, request):
        lote_id = request.data.get('lote_id')
        
        try:
            lote = Lote.objects.get(id=lote_id)
        except Lote.DoesNotExist:
            return Response({'error': 'Lote não encontrado'}, status=404)
        
        if Entrada.objects.filter(lote=lote).exists():
            return Response({'message': 'Parcelas já geradas para este lote'})
        
        data_parcelas = lote.data_parcelas
        numero_parcelas = lote.numero_parcelas
        valor_inicial = lote.valor_inicial
        
        parcelas = []
        valor_parcela = valor_inicial / numero_parcelas
        data_projecao = data_parcelas
        
        for i in range(numero_parcelas):
            parcela = {
                'vencimento': data_projecao,
                'parcela': i + 1,
                'valor_a_receber': valor_parcela
            }
            parcelas.append(parcela)
            
            # Incrementa a data para o próximo mês
            data_projecao += relativedelta(months=1)
        
        # Salva as entradas projetadas na tabela Entrada
        for parcela in parcelas:
            entrada = Entrada(
                lote=lote,
                vencimento=parcela['vencimento'],
                parcela=parcela['parcela'],
                valor_a_receber=parcela['valor_a_receber']
            )
            entrada.save()
        
        return Response({'parcelas': parcelas})
    

class AtualizarValorParcelasAPIView(APIView):
    def post(self, request):
        numero_parcela = request.data.get('numero_parcela')
        lote_id = request.data.get('lote_id')
        novo_valor_str = request.data.get('novo_valor')
        print('numero_parcela')
        print(numero_parcela)
        print(lote_id)
        print(novo_valor_str)

        try:
            lote = Lote.objects.get(id=lote_id)
        except Lote.DoesNotExist:
            return Response({'error': 'Lote não encontrado'}, status=404)
        
        try:
            novo_valor = Decimal(novo_valor_str)
        except (ValueError, TypeError):
            return Response({'error': 'Valor inválido'}, status=400)

        parcelas = Entrada.objects.filter(lote=lote, parcela__gte=numero_parcela)
        if not parcelas:
            return Response({'error': 'Parcelas não encontradas'}, status=404)

        for parcela in parcelas:
            parcela.valor_a_receber += novo_valor
            parcela.save()

        return Response({'message': 'Valor das parcelas atualizado com sucesso'})