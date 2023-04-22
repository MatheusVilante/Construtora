from django.db import models

class ControleFuncionario(models.Model):
    DIAS_DA_SEMANA = [
        ('Segunda', 'Segunda-feira'),
        ('Terca', 'Terça-feira'),
        ('Quarta', 'Quarta-feira'),
        ('Quinta', 'Quinta-feira'),
        ('Sexta', 'Sexta-feira'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo')
    ]

    funcionario = models.CharField(max_length=100)
    dias = models.CharField(max_length=10, choices=DIAS_DA_SEMANA)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    periodo = models.DateField()

    def __str__(self):
        return f"{self.funcionario} - {self.dias} - {self.periodo}"
