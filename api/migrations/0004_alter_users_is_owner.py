# Generated by Django 5.1.1 on 2024-09-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_users_is_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='é proprietario?'),
        ),
    ]
