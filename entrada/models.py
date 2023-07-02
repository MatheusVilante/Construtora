from django.utils import timezone
from django.db import models


class Entrada(models.Model):
    lote = models.ForeignKey('quadraLote.Lote', on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        'cliente.Cliente',
        verbose_name='cliente',
        related_name='ClienteEntrada',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    observacoes = models.CharField(max_length=100,null=True, blank=True)
    banco = models.CharField(max_length=100,null=True, blank=True)
    data = models.DateField(max_length=100,null=True, blank=True)
    tipo_transferencia = models.CharField(max_length=100,null=True, blank=True)
    situacao = models.CharField(max_length=100, null=True, blank=True)
    vencimento = models.DateField(null=True, blank=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_a_receber = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_boleto_empresa = models.CharField(max_length=100, null=True, blank=True)
    numero_boleto_cliente = models.CharField(max_length=100, null=True, blank=True)
    parcela = models.CharField(max_length=100 ,null=True, blank=True)



    def _str_(self):
        return f'{self.lote_id} - {self.parcela}'
    
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'