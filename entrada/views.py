from django.http import JsonResponse
from rest_framework import viewsets
from .models import Entrada
from .serializers import EntradaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import ExtractDay
from datetime import date, timedelta



class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    

class ClientePagamentoView(APIView):
    def get(self, request):
        id = request.GET.get("id")
        parametro = Entrada.objects.filter(lote_id=id)
        serializer_class = EntradaSerializer(parametro, many=True)
        return Response(serializer_class.data)
    
class GraficoEntradaView(APIView):
    def get(self, request):
        today = date.today()
        month = today.month
        year = today.year

        # Obter o primeiro dia do mês atual
        first_day = date(year, month, 1)

        # Obter o último dia do mês atual
        next_month = first_day.replace(day=28) + timedelta(days=4)
        last_day = next_month - timedelta(days=next_month.day)

        # Criar uma lista com todos os dias do mês
        dias_do_mes = [first_day + timedelta(days=i) for i in range((last_day - first_day).days + 1)]

        # Query para buscar os valores diários da tabela "entrada" para o mês atual
        dados_gastos_diarios = (
            Entrada.objects.filter(vencimento__month=month, vencimento__year=year)
            .annotate(dia=ExtractDay('vencimento'))
            .values('dia')
            .annotate(valor=Sum('valor_pago'))
            .order_by('dia')
        )

        # Converter os resultados em um dicionário com os valores diários
        gastos_diarios = {dia.day: 0 for dia in dias_do_mes}
        for dados in dados_gastos_diarios:
            dia = dados['dia']
            valor = dados['valor']
            gastos_diarios[dia] = valor

        # Converter o dicionário em uma lista de dicionários
        gastos_diarios_list = [{'dia': dia, 'valor': gastos_diarios[dia]} for dia in gastos_diarios]

        # Responder com os dados em formato JSON
        return JsonResponse(gastos_diarios_list, safe=False)