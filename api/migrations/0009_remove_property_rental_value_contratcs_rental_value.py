# Generated by Django 5.1.1 on 2024-09-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_available_property_avaliable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='rental_value',
        ),
        migrations.AddField(
            model_name='contratcs',
            name='rental_value',
            field=models.FloatField(default=0, verbose_name='Valor de aluguel'),
        ),
    ]
