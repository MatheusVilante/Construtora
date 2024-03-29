# Generated by Django 3.2.18 on 2023-05-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controledeCheque', '0003_auto_20230509_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlecheque',
            name='agencia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='banco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='conta_corrente',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='numero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='controlecheque',
            name='vencimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
