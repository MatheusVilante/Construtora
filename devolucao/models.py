from django.db import models
from django.utils import timezone
from quadraLote.models import Lote

class Devolucao(models.Model):
    lote_id = models.ForeignKey(Lote, on_delete=models.CASCADE)
    data_restituicao = models.DateTimeField(default=timezone.now)
    valor_restituir = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento = models.CharField(max_length=100)
    parcela = models.IntegerField()

    excluido = models.BooleanField(default=False)
    data_exclusao = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.excluido = True
        self.data_exclusao = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "Devolucoes"
        ordering = ['id']

class DevolucaoParcela(models.Model):
    devolucao_id = models.ForeignKey(Devolucao, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_referencia = models.DateField()
    data_pagamento = models.DateField()

    excluido = models.BooleanField(default=False)
    data_exclusao = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.excluido = True
        self.data_exclusao = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "DevolucoesParcela"
        ordering = ['id']
