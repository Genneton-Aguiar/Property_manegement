# Generated by Django 5.1.1 on 2024-09-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_tenants_contract_remove_tenants_property_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_owner',
            field=models.BooleanField(default=False, null=True, verbose_name='é proprietario?'),
        ),
    ]
