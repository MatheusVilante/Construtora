from django.conf.urls import url
from django.urls import path

from .views import clienteLote, controleFuncionario, dadosIniciais, depositoCliente, despesa, devolucao, documentoEnviado, fluxo, historico, imposto, index, cliente, inicio, login, lote, quadra, situacaodePagamento, clientePagamento, controledeCheque, disponibilidade


urlpatterns = [
    path('index', index, name='index'),
    path('login', login, name='login'),
    path('cliente', cliente, name='cliente'),
    path('quadra', quadra, name='quadra'),
    path('lote', lote, name='lote'),
    path('situacaodePagamento', situacaodePagamento, name='situacaodePagamento'),
    path('clienteLote', clienteLote, name='clienteLote'),
    path('clientePagamento', clientePagamento, name='clientePagamento'),
    path('controledeCheque', controledeCheque, name='controledeCheque'),
    path('dadosIniciais', dadosIniciais, name='dadosIniciais'),
    path('depositoCliente', depositoCliente, name='depositoCliente'),
    path('disponibilidade', disponibilidade, name='disponibilidade'),
    path('historico', historico, name='historico'),
    path('documentoEnviado', documentoEnviado, name='documentoEnviado'),
    path('despesa', despesa, name='despesa'),
    path('controleFuncionario', controleFuncionario, name='controleFuncionario'),
    path('imposto', imposto, name='imposto'),
    path('devolucao', devolucao, name='devolucao'),
    path('inicio', inicio, name='inicio'),
    path('fluxo', fluxo, name='fluxo'),
]