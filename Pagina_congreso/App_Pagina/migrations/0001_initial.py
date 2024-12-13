# Generated by Django 5.1.4 on 2024-12-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('codigo_postal', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Resumenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField(max_length=500)),
                ('poster', models.BooleanField()),
                ('fecha_revision', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Revisores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('area', models.CharField(max_length=20)),
            ],
        ),
    ]
