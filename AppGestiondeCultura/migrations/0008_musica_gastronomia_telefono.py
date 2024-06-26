# Generated by Django 5.0.6 on 2024-06-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestiondeCultura', '0007_rename_edad_cine_edad_minima'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=35)),
                ('genero', models.CharField(max_length=50)),
                ('edad_minima', models.IntegerField()),
                ('pais_origen', models.CharField(max_length=35)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]
