# Generated by Django 3.2.18 on 2023-05-18 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleFuncionario', '0003_auto_20230517_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlefuncionario',
            old_name='data_final',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='controlefuncionario',
            name='data_inicial',
        ),
        migrations.RemoveField(
            model_name='controlefuncionario',
            name='dias',
        ),
    ]
