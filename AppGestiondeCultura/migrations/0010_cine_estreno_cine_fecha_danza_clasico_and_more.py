# Generated by Django 5.0.6 on 2024-06-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestiondeCultura', '0009_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='cine',
            name='estreno',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='cine',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='danza',
            name='clasico',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='danza',
            name='independiente',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='apto_veganos',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='teatro',
            name='autor',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teatro',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
