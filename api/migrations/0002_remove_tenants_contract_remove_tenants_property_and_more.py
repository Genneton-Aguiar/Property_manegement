# Generated by Django 5.1.1 on 2024-09-11 19:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenants',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='tenants',
            name='property',
        ),
        migrations.RemoveField(
            model_name='tenants',
            name='user',
        ),
        migrations.AddField(
            model_name='contratcs',
            name='date_limit',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data limite de pagamento'),
        ),
        migrations.AlterField(
            model_name='contratcs',
            name='adjustments',
            field=models.FloatField(default=0, verbose_name='reajustes previstos'),
        ),
        migrations.AlterField(
            model_name='contratcs',
            name='validity',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='vigencia do contrato'),
        ),
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.users', verbose_name='proprietario'),
        ),
        migrations.CreateModel(
            name='Repasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payments', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.payments', verbose_name='Pagamento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.users', verbose_name='proprietario')),
            ],
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
        migrations.DeleteModel(
            name='Tenants',
        ),
    ]
