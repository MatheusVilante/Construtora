from django.db import models

class ControleCheque(models.Model):
    lote_id = models.IntegerField()
    nome = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=100)
    conta_corrente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return f'{self.lote_id} - {self.numero}'
    
    class Meta:
        verbose_name = 'Controle de Cheque'
        verbose_name_plural = 'Controle de Cheques'