# Generated by Django 3.2.18 on 2023-04-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='numero_boleto_cliente',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='numero_boleto_empresa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='observacoes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='parcela',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='situacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='valor_a_receber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='valor_pago',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='vencimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
