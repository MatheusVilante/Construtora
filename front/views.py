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



