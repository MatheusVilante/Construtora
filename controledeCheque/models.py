from django.db import models

class ControleCheque(models.Model):
    lote = models.ForeignKey(
        'quadraLote.Lote',
        verbose_name='lote',
        related_name='LoteControleCheque',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    cliente = models.ForeignKey(
        'cliente.Cliente',
        verbose_name='cliente',
        related_name='ClienteControleCheque',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    banco = models.CharField(max_length=100, null=True, blank=True)
    agencia = models.CharField(max_length=100, null=True, blank=True)
    conta_corrente = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=100, null=True, blank=True)
    vencimento = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    observacoes = models.CharField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return f'{self.lote_id} - {self.numero}'
    
    class Meta:
        verbose_name = 'Controle de Cheque'
        verbose_name_plural = 'Controle de Cheques'