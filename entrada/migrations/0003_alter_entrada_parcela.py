# Generated by Django 3.2.18 on 2023-05-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_auto_20230429_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='parcela',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
