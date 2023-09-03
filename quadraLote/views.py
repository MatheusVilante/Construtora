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
        numero_parcelas = int(request.POST.get("numero_parcelas"))
        data_de_vencimento = datetime.strptime(request.POST.get("data_de_vencimento"), "%Y-%m-%d").date()
        valor = float(request.POST.get("valor").replace(",", "."))
        numero_you = int(request.POST.get("numero_you"))
        numero_i = int(request.POST.get("numero_i"))
        numero_do_carne = request.POST.get("numero_do_carne")
        lote_id = request.POST.get("lote_id")
        tipo_parcela = request.POST.get("tipo_parcela")  # Adicione este campo

        # Verifique se o tipo de parcela não é "int" ou "ent" para determinar a sequência
        if tipo_parcela != "int" and tipo_parcela != "ent":
            parcelas_existentes = Entrada.objects.filter(lote_id=lote_id).exclude(parcela__contains="INT.").exclude(parcela__contains="ENT.")
            if parcelas_existentes.exists():
                ultimo_numero_parcela_existente = max([int(p.parcela) for p in parcelas_existentes])
                numero_primeira_parcela = ultimo_numero_parcela_existente + 1
            else:
                numero_primeira_parcela = 1
        else:
            numero_primeira_parcela = 1

        # Gerar as parcelas
        parcelas = []
        for numero_parcela in range(numero_primeira_parcela, numero_primeira_parcela + numero_parcelas):
            if tipo_parcela == "int":
                parcelas_existentes_int = Entrada.objects.filter(lote_id=lote_id, parcela__contains="INT.").exclude(parcela__contains="ENT.")
                if parcelas_existentes_int.exists():
                    # Encontre a parcela "int" com o maior número
                    ultima_parcela_int = max([int(p.parcela.split('.')[1].split('-')[0]) for p in parcelas_existentes_int])
                    numero_int = ultima_parcela_int + 1
                else:
                    numero_int = 1

                # Construa a parcela no formato correto
                ano_intercalada = data_de_vencimento.year
                numero_parcela_formatado = f"INT.{numero_int}-{ano_intercalada}"

            elif tipo_parcela == "ent":
                numero_entrada = numero_parcela - numero_primeira_parcela + 1
                numero_parcela_formatado = f"ENT.{numero_entrada}"  

            else:  # Parcela comum
                numero_parcela_formatado = numero_parcela

            vencimento = data_de_vencimento + relativedelta(months=numero_parcela - numero_primeira_parcela)
            parcela = {
                "numero": numero_parcela_formatado,
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
                parcela=numero_parcela_formatado,
                situacao='aberta'
            )
            entrada.save()
        # Retornar as parcelas
        return Response(parcelas)


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