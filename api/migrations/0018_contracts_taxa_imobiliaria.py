# Generated by Django 5.1.1 on 2024-09-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_rename_user_contracts_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='taxa_imobiliaria',
            field=models.FloatField(default=0.3, verbose_name='Taxa da imobiliaria'),
        ),
    ]
