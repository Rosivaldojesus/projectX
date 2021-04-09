# Generated by Django 3.0 on 2021-04-06 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('componentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('adm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.Administradora')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.Cidade')),
                ('fabricanteCFTV', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.FabricanteCFTV')),
                ('fabricanteSAI', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.FabricanteSAI')),
                ('fabricanteSAP', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.FabricanteSAP')),
                ('fabricanteSCA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.FabricanteSCA')),
                ('fabricanteSDAI', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.FabricanteSDAI')),
            ],
        ),
    ]