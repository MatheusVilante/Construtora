from django.db import models

class ControleFuncionario(models.Model):


    funcionario = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.funcionario} "
