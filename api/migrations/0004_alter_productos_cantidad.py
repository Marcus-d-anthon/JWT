# Generated by Django 5.1.6 on 2025-02-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_productos_fecha_vencimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Cantidad',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
