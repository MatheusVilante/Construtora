# Generated by Django 3.2.18 on 2023-03-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imposto', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('situacao', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=255)),
                ('valor_devolvido', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_retirado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('data_rescisao', models.DateField(blank=True, null=True)),
                ('data_quitacao', models.DateField(blank=True, null=True)),
                ('saldo_devedor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('id_lote', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
            },
        ),
    ]
