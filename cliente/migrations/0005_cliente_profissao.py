# Generated by Django 3.2.18 on 2023-06-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20230427_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]