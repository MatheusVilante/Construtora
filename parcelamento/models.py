from django.db import models
from django.utils import timezone

class Parcelamento(models.Model):
    tipo = models.CharField(max_length=50)
    meses = models.IntegerField()
    numero_intercalada = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    parcela = models.DecimalField(max_digits=10, decimal_places=2)
    intercalada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entrada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    excluido = models.BooleanField(default=False)
    data_exclusao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} ({self.id})"

    def delete(self):
        self.excluido = True
        self.data_exclusao = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "Parcelamentos"
        ordering = ['id']
