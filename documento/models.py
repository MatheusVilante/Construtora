from django.db import models
from quadraLote.models import Lote
from cliente.models import Cliente

class Documento(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=50)
    situacao = models.CharField(max_length=50)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_documento} do cliente {self.cliente.nome} ({self.lote.nome})"

    class Meta:
        verbose_name_plural = "Documentos"

class Historico(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500)
    data = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Historicos"
