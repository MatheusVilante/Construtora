from django.utils import timezone
from django.db import models


class Entrada(models.Model):
    lote = models.ForeignKey('quadraLote.Lote', on_delete=models.CASCADE)
    data = models.DateField()
    banco = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor_devido = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)
    parcela = models.IntegerField()
    cpf_cnpj = models.CharField(max_length=100)
    total_recebido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    formas_pagamento = models.TextField(null=True, blank=True)
    transacao = models.CharField(max_length=100, null=True, blank=True)
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=2)
    debito_intercalada = models.CharField(max_length=100, null=True, blank=True)
    preco_intercalada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_intercaladas = models.IntegerField(null=True, blank=True)
    debito_parcelas_aas = models.CharField(max_length=100, null=True, blank=True)
    numero_parcelas_aas = models.IntegerField(null=True, blank=True)
    preco_carne = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parcelas = models.IntegerField()
    entrada = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.CharField(max_length=100,null=True, blank=True)
    situacao = models.CharField(max_length=100, null=True, blank=True)
    vencimento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_a_receber = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_boleto_empresa = models.CharField(max_length=100, null=True, blank=True)
    numero_boleto_cliente = models.CharField(max_length=100, null=True, blank=True)
    data_contrato = models.DateField()
    codigo_parcela = models.CharField(max_length=100)
    parcela = models.IntegerField()
    tipo_parcela = models.CharField(max_length=100)
    data_vencimento = models.DateField()
    valor_corrigido = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)
    fracao_ideal = models.DecimalField(max_digits=10, decimal_places=2)
    indexador = models.CharField(max_length=100)
    taxa_juros = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField()
    cpf_cnpj_comprador = models.CharField(max_length=100)
    nome_comprador = models.CharField(max_length=100)
    data_habite_se = models.DateField(null=True, blank=True)
    performado = models.CharField(max_length=100)
    bloco = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    fase = models.CharField(max_length=100)
    empreendimento = models.CharField(max_length=100)
    codigo_contrato_id = models.CharField(max_length=100)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    excluido = models.BooleanField(default=False)
    data_exclusao = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.excluido = True
        self.data_exclusao = timezone.now()
        self.save()

    def _str_(self):
        return f'{self.lote_id} - {self.parcela}'
    
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'