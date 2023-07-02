# Generated by Django 3.2.18 on 2023-04-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20230318_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together={('nome', 'cpf')},
        ),
    ]