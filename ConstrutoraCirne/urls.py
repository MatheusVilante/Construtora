from django.contrib import admin
from django.urls import path,include
import dropbox
from dropbox.urls import *
import front.urls
from rest_framework.routers import SimpleRouter
from cliente.views import ClienteViewSet
from despesas.views import DespesaViewSet
from entrada.views import EntradaViewSet
from controledeCheque.views import ControleChequeViewSet
from quadraLote.views import QuadraViewSet, LoteViewSet
from controleFuncionario.views import ControleFuncionarioViewSet
from documento.views import DocumentoViewSet
from parcelamento.views import ParcelamentoViewSet
from devolucao.views import DevolucaoViewSet, DevolucaoParcelaViewSet


router = SimpleRouter()
router.register(r'despesa', DespesaViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'entrada', EntradaViewSet)
router.register(r'controlecheque', ControleChequeViewSet)
router.register(r'quadra', QuadraViewSet)
router.register(r'lote', LoteViewSet)
router.register(r'controlefuncionario', ControleFuncionarioViewSet)
router.register(r'documento', DocumentoViewSet)
router.register(r'parcelamento', ParcelamentoViewSet)
router.register(r'devolucao', DevolucaoViewSet)
router.register(r'devolucaoparcela', DevolucaoParcelaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include(front.urls)),
    path('', include(dropbox.urls)),

]