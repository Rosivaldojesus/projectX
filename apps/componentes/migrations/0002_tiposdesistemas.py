# Generated by Django 3.0 on 2021-04-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposDeSistemas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiposSistemas', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Sistemas',
            },
        ),
    ]