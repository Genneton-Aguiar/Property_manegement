# Generated by Django 5.1.1 on 2024-09-27 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_repasse_imobiliaria_value_repasse_proprietario_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='user',
            new_name='owner',
        ),
    ]
