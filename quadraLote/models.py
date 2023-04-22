from django.db import models
from cliente.models import Cliente

class Quadra(models.Model):
    quadra = models.CharField(max_length=100)
    
    def __str__(self):
        return self.quadra
    
    class Meta:
        verbose_name = 'Quadra'
        verbose_name_plural = 'Quadras'

class Lote(models.Model):
    quadra_Id = models.ForeignKey(Quadra, on_delete=models.CASCADE)
    lote = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento_id = models.CharField(max_length=100)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aditivo_de_alteracao = models.CharField(max_length=100)
    numero_da_matricula = models.CharField(max_length=100)
    data_de_venda = models.DateField()
    periodicidade_de_reajuste = models.CharField(max_length=100)
    sistema_de_amortizacao = models.CharField(max_length=100)
    taxa_de_juros = models.DecimalField(max_digits=10, decimal_places=2)
    indexador_apos_habitase = models.CharField(max_length=100)
    indexador_ate_habitase = models.CharField(max_length=100)
    prazo_total = models.IntegerField()
    valor_de_financiamento = models.DecimalField(max_digits=10, decimal_places=2)
    valor_de_avaliacao = models.DecimalField(max_digits=10, decimal_places=2)
    valor_de_venda = models.DecimalField(max_digits=10, decimal_places=2)
    fracao_ideal = models.CharField(max_length=100)
    nome_do_empreendimento = models.CharField(max_length=100)
    spe = models.CharField(max_length=100)
    tipo_de_contrato = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    tipo_de_imovel = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    nome_devedor = models.CharField(max_length=100)
    tipos_de_cliente = models.CharField(max_length=100)
    codigo_de_contrato = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.lote}'
    
    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'