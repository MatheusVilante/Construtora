from django.db import models
from quadraLote.models import Lote


class Despesa(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=True)
    data_referencia = models.DateField(null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    imposto = models.CharField(max_length=100 ,null=True, blank=True)
    codigo = models.CharField(max_length=100, null=True, blank=True)
    vencimento = models.DateField( null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    situacao = models.CharField(max_length=100 ,null=True, blank=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    observacao = models.CharField(max_length=255 ,null=True, blank=True)
    valor_devolvido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_retirado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    data_quitacao = models.DateField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    devolucao = models.BooleanField(default=False)
    geral = models.BooleanField(default=False)


    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'