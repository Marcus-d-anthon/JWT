# Generated by Django 5.1.6 on 2025-02-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Fecha_empaquetado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='Fecha_vencimiento',
            field=models.DateTimeField(),
        ),
    ]
