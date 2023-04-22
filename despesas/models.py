from django.db import models

class Despesa(models.Model):
    imposto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255)
    valor_devolvido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_retirado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    data_quitacao = models.DateField(null=True, blank=True)
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    id_lote = models.IntegerField()

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'