from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView



def index(request):
    return render(request, 'pages/index.html')

def cliente(request):
    return render(request, 'pages/cliente.html')

def lote(request):
    return render(request, 'pages/lote.html')

def quadra(request):
    return render(request, 'pages/quadra.html')

def clienteLote(request):
    return render(request, 'pages/clienteLote.html')

def situacaodePagamento(request):
    return render(request, 'pages/situacaodePagamento.html')

def clientePagamento(request):
    return render(request, 'pages/clientePagamento.html')

def controledeCheque(request):
    return render(request, 'pages/controledeCheque.html')

def dadosIniciais(request):
    return render(request, 'pages/dadosIniciais.html')

def depositoCliente(request):
    return render(request, 'pages/depositoCliente.html')

def disponibilidade(request):
    return render(request, 'pages/disponibilidade.html')

def documentoEnviado(request):
    return render(request, 'pages/documentoEnviado.html')

def historico(request):
    return render(request, 'pages/historico.html')

def despesa(request):
    return render(request, 'pages/despesa.html')

def controleFuncionario(request):
    return render(request, 'pages/controleFuncionario.html')

def imposto(request):
    return render(request, 'pages/imposto.html')

def devolucao(request):
    return render(request, 'pages/devolucao.html')

def inicio(request):
    return render(request, 'pages/inicio.html')

def fluxo(request):
    return render(request, 'pages/fluxo.html')
