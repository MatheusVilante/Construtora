from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

@login_required
def cliente(request):
    return render(request, 'pages/cliente.html')

@login_required
def lote(request):
    return render(request, 'pages/lote.html')

@login_required
def quadra(request):
    return render(request, 'pages/quadra.html')

@login_required
def clienteLote(request):
    return render(request, 'pages/clienteLote.html')

@login_required
def situacaodePagamento(request):
    return render(request, 'pages/situacaodePagamento.html')

@login_required
def clientePagamento(request):
    return render(request, 'pages/clientePagamento.html')

@login_required
def controledeCheque(request):
    return render(request, 'pages/controledeCheque.html')

@login_required
def dadosIniciais(request):
    return render(request, 'pages/dadosIniciais.html')

@login_required
def depositoCliente(request):
    return render(request, 'pages/depositoCliente.html')

@login_required
def disponibilidade(request):
    return render(request, 'pages/disponibilidade.html')

@login_required
def documentoEnviado(request):
    return render(request, 'pages/documentoEnviado.html')

@login_required
def historico(request):
    return render(request, 'pages/historico.html')

@login_required
def despesa(request):
    return render(request, 'pages/despesa.html')

@login_required
def controleFuncionario(request):
    return render(request, 'pages/controleFuncionario.html')

@login_required
def imposto(request):
    return render(request, 'pages/imposto.html')

@login_required
def devolucao(request):
    return render(request, 'pages/devolucao.html')
    
@login_required
def inicio(request):
    return render(request, 'pages/inicio.html')
    
@login_required
def fluxo(request):
    return render(request, 'pages/fluxo.html')
