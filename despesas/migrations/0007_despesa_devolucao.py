# Generated by Django 3.2.18 on 2023-05-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0006_auto_20230518_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='devolucao',
            field=models.BooleanField(default=False),
        ),
    ]
