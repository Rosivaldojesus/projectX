# Generated by Django 3.0 on 2021-04-08 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_equipamentoscliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamentoscliente',
            name='equipamentoCliente',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]