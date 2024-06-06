# Generated by Django 5.0.6 on 2024-06-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestiondeCultura', '0004_cine_gastronomia'),
    ]

    operations = [
        migrations.AddField(
            model_name='danza',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='probado',
            field=models.BooleanField(null=True),
        ),
    ]