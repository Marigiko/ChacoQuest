# Generated by Django 4.2.6 on 2023-10-04 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_pregunta_fecha_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='fecha_categoria',
        ),
    ]