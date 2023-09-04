from django.contrib import admin
from django.urls import path,include
from documento.serializers import DocumentoReadSerializer
import dropbox
from dropbox.urls import *
import front.urls
from rest_framework.routers import SimpleRouter
from cliente.views import ClienteViewSet
from despesas.views import DespesaViewSet, LeituraDespesaViewSet, ParcelasView
from entrada.views import ClientePagamentoView, EntradaViewSet, GraficoEntradaView
from controledeCheque.views import ControleChequeViewSet
from quadraLote.views import AtualizarValorParcelasAPIView, FluxoViewSet, ProjecaoParcelasView, QuadraViewSet, LoteViewSet, ClienteLoteView, Disponibilidade
from controleFuncionario.views import ControleFuncionarioViewSet
from documento.views import DocumentoViewSet, HistoricoViewSet
from parcelamento.views import ParcelamentoViewSet
from devolucao.views import DevolucaoViewSet, DevolucaoParcelaViewSet
from usuario.views import UsuarioAPIView


router = SimpleRouter()
router.register(r'fluxo', FluxoViewSet)
router.register(r'despesa', DespesaViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'entrada', EntradaViewSet)
router.register(r'controlecheque', ControleChequeViewSet)
router.register(r'quadra', QuadraViewSet)
router.register(r'lote', LoteViewSet)
router.register(r'controlefuncionario', ControleFuncionarioViewSet)
router.register(r'documento', DocumentoViewSet)
# router.register(r'documentoread', DocumentoReadSerializer, basename='documentoread')
router.register(r'parcelamento', ParcelamentoViewSet)
router.register(r'devolucao', DevolucaoViewSet)
router.register(r'devolucaoparcela', DevolucaoParcelaViewSet)
router.register(r'historico', HistoricoViewSet)
router.register(r'leituraDespesa', LeituraDespesaViewSet)
# router.register(r'leituraDespesa', DocumentoReadViewSet)

urlpatterns = [
    path('vincularLote/', ClienteLoteView.as_view()),
    path('api/v1/login/', UsuarioAPIView.as_view()),
    path('atualizarParcelas/', AtualizarValorParcelasAPIView.as_view()),
    path('projetarParcelas/', ProjecaoParcelasView.as_view()),
    path('graficoEntrada/', GraficoEntradaView.as_view()),
    path('disponibilidade/', Disponibilidade.as_view()),
    path('clientePagamento/', ClientePagamentoView.as_view()),
    path('parcelas/', ParcelasView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include(front.urls)),
    path('', include(dropbox.urls)),
]