# Generated by Django 3.0 on 2021-04-06 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerguntaForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_pergunta', models.CharField(blank=True, max_length=255, null=True)),
                ('pergunta_forum', models.CharField(blank=True, max_length=251, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pergunta Fórum',
            },
        ),
        migrations.CreateModel(
            name='RespostaForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(blank=True, max_length=253, null=True)),
                ('resposta_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.PerguntaForum')),
            ],
            options={
                'verbose_name_plural': 'Resposta Fórum',
            },
        ),
    ]