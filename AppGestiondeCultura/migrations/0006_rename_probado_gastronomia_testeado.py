# Generated by Django 5.0.6 on 2024-06-04 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestiondeCultura', '0005_danza_fecha_gastronomia_probado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gastronomia',
            old_name='probado',
            new_name='testeado',
        ),
    ]