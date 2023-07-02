from rest_framework import viewsets

from quadraLote.models import Lote
from .models import Despesa
from .serializers import DespesaSerializer, LeituraDespesaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from dateutil.relativedelta import relativedelta

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    
    
class LeituraDespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = LeituraDespesaSerializer

class ParcelasView(APIView):
    def get(self, request):
        lote_id = request.POST.get('lote')
        print(lote_id)
        despesas = Despesa.objects.filter(lote_id=lote_id, devolucao=True)  # Filtrando por lote__lote
        dados_despesas = []
        # print(despesas)
        for despesa in despesas:
            # Adicionando os campos que deseja retornar
            dados_despesas.append({
                'valor': despesa.valor,
                'data': despesa.data,
                'lote': despesa.lote.lote,  # Acessando o campo 'lote' da tabela Lote através da chave estrangeira
            })
        
        return Response(dados_despesas)
    def post(self, request):
        data_recisao = request.POST.get('data_recisao')
        lote_id = request.POST.get('lote')
        valor_devolver = float(request.POST.get('valor_devolver'))
        num_parcelas = int(request.POST.get('num_parcelas'))
        print(valor_devolver)

        parcelas = []

        valor_parcela = valor_devolver / num_parcelas
        data_parcela = datetime.strptime(data_recisao, '%Y-%m-%d')

        for i in range(1, num_parcelas + 1):
            parcela = {
                
                'parcela': i,
                'valor': valor_parcela,
                'data': data_parcela.strftime('%Y-%m-%d')
            }
            parcelas.append(parcela)

            # Incrementa a data da parcela em um mês
            data_parcela += relativedelta(months=1)
            
            lote = Lote.objects.get(id=lote_id)
            
            
            despesa = Despesa(valor=valor_parcela, data=data_parcela, devolucao=True,lote_id=lote.id,situacao = "aberto")
            despesa.save()


        return Response(parcelas)