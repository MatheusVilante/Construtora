from django.db import models
from cliente.models import Cliente

class Quadra(models.Model):
    residencial = models.CharField(max_length=100)
    quadra = models.CharField(max_length=100)
    
    def __str__(self):
        return self.quadra
    
    class Meta:
        verbose_name = 'Quadra'
        verbose_name_plural = 'Quadras'

class Lote(models.Model):
    quadra = models.ForeignKey(
        'quadraLote.Quadra',
        verbose_name='quadra',
        related_name='QuadraLote',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    cliente = models.ForeignKey(
        'cliente.Cliente',
        verbose_name='cliente',
        related_name='ClienteLote',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )      
    disponibilidade = models.BooleanField(default=True)         
    lote = models.CharField(max_length=100, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    parcelamento_id = models.CharField(max_length=100, blank=True, null=True)
    aditivo_de_alteracao = models.CharField(max_length=100, blank=True, null=True)
    numero_da_matricula = models.CharField(max_length=100, blank=True, null=True)
    data_de_venda = models.DateField(blank=True, null=True)
    data_de_habita = models.DateField(blank=True, null=True)
    periodicidade_de_reajuste = models.CharField(max_length=100, blank=True, null=True)
    sistema_de_amortizacao = models.CharField(max_length=100, blank=True, null=True)
    taxa_de_juros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    indexador_apos_habitase = models.CharField(max_length=100, blank=True, null=True)
    indexador_ate_habitase = models.CharField(max_length=100, blank=True, null=True)
    prazo_total = models.IntegerField(blank=True, null=True)
    valor_financiamento_pre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_financiamento_pos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_de_avaliacao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_de_venda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fracao_ideal = models.CharField(max_length=100, blank=True, null=True)
    nome_do_empreendimento = models.CharField(max_length=100, blank=True, null=True)
    spe = models.CharField(max_length=100, blank=True, null=True)
    tipo_de_contrato = models.CharField(max_length=100, blank=True, null=True)
    numero_contrato = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    tipo_de_imovel = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    nome_devedor = models.CharField(max_length=100, blank=True, null=True)
    tipos_de_cliente = models.CharField(max_length=100, blank=True, null=True)
    codigo_de_contrato = models.CharField(max_length=100, blank=True, null=True)
    data_parcelas = models.DateField(blank=True, null=True)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    numero_parcelas = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.lote}'
    
    def save(self, *args, **kwargs):
        if self.cliente:
            self.disponibilidade = False
        else:
            self.disponibilidade = True
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'