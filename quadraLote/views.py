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
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

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
        quadras = Quadra.objects.prefetch_related('QuadraLote')

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

        return JsonResponse(estoque, safe=False)
    


class ProjecaoParcelasView(APIView):
    def post(self, request):
        numero_primeira_parcela = int(request.POST.get("numero_primeira_parcela"))
        numero_ultima_parcela = int(request.POST.get("numero_ultima_parcela"))
        data_de_vencimento = datetime.strptime(request.POST.get("data_de_vencimento"), "%Y-%m-%d").date()
        valor = float(request.POST.get("valor").replace(",", "."))
        numero_you = int(request.POST.get("numero_you"))
        numero_i = int(request.POST.get("numero_i"))
        numero_do_carne = request.POST.get("numero_do_carne")
        lote_id = request.POST.get("lote_id")

        parcelas_existentes = Entrada.objects.filter(lote_id=lote_id, parcela__lte=numero_ultima_parcela)
        print(parcelas_existentes)
        if parcelas_existentes.exists():
            ultimo_numero_parcela_existente = parcelas_existentes.last().parcela
            # print(ultimo_numero_parcela_existente)
            proximo_numero_esperado = int(ultimo_numero_parcela_existente) + 1
            # print(proximo_numero_esperado)

            if numero_primeira_parcela != proximo_numero_esperado:
                # print("numero errado")
                return Response({
                    "error": f"O primeiro número da parcela deve ser {proximo_numero_esperado}"
                })

        # Gerar as parcelas
        parcelas = []
        for numero_parcela in range(numero_primeira_parcela, numero_ultima_parcela + 1):
            vencimento = data_de_vencimento + relativedelta(months=numero_parcela - numero_primeira_parcela)  # Incrementa 1 mês para cada parcela
            parcela = {
                "numero": numero_parcela,
                "vencimento": vencimento,
                "valor": valor,
                "nosso_numero": f"{numero_do_carne}/{numero_parcela + numero_i - numero_primeira_parcela}",
                "seu_numero": numero_you + numero_parcela - numero_primeira_parcela
            }
            parcelas.append(parcela)
            entrada = Entrada.objects.create(
                lote_id=lote_id,
                vencimento=vencimento,
                valor_a_receber=valor,
                numero_boleto_cliente=parcela["seu_numero"],
                numero_boleto_empresa=parcela["nosso_numero"],
                parcela=numero_parcela
            )
            # print(entrada)
            entrada.save()

        # Retornar as parcelas
        return Response(parcelas)


    #     lote_id = request.data.get('lote_id')

    #     try:
    #         lote = Lote.objects.get(id=lote_id)
    #     except Lote.DoesNotExist:
    #         return Response({'error': 'Lote não encontrado'}, status=404)

    #     if Entrada.objects.filter(lote=lote).exists():
    #         return Response({'message': 'Parcelas já geradas para este lote'})

    #     data_parcelas = lote.data_parcelas
    #     numero_parcelas = lote.numero_parcelas
    #     valor_inicial = lote.valor_inicial
        
    #     parcelas = []
    #     valor_parcela = valor_inicial / numero_parcelas
    #     data_projecao = data_parcelas

    #     for i in range(numero_parcelas):
    #         parcela = {
    #             'vencimento': data_projecao,
    #             'parcela': i + 1,
    #             'valor_a_receber': valor_parcela
    #         }
    #         parcelas.append(parcela)
    #         data_projecao += relativedelta(months=1)

    #     for parcela in parcelas:
    #         entrada = Entrada(
    #             lote=lote,
    #             vencimento=parcela['vencimento'],
    #             parcela=parcela['parcela'],
    #             valor_a_receber=parcela['valor_a_receber']
    #         )
    #         entrada.save()

    #     return Response({'parcelas': parcelas})    

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