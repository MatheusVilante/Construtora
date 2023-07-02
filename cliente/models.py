from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    dataNascimento = models.DateField(blank=True, null=True)
    contratoNovo = models.CharField(max_length=100, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    datadeAssinatura = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    intercalada = models.CharField(max_length=100, blank=True, null=True)
    profissao = models.CharField(max_length=100,null=True, blank=True)
    rg = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nome

    
    class Meta:
        unique_together = ('nome', 'cpf')
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    
    