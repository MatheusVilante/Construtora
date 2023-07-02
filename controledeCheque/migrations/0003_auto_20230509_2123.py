# Generated by Django 3.2.18 on 2023-05-10 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20230427_2237'),
        ('controledeCheque', '0002_auto_20230509_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlecheque',
            name='nome',
        ),
        migrations.AddField(
            model_name='controlecheque',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ClienteControleCheque', to='cliente.cliente', verbose_name='cliente'),
        ),
    ]