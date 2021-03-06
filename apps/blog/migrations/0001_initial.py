# Generated by Django 3.0 on 2021-04-19 15:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_post', models.CharField(max_length=255)),
                ('data_post', models.DateTimeField(default=datetime.datetime(2021, 4, 19, 15, 41, 32, 394533, tzinfo=utc))),
                ('conteudo_post', models.TextField()),
                ('excerto_post', models.TextField()),
                ('publicado_post', models.BooleanField(default=False)),
                ('autor_post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('categoria_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Categoria')),
            ],
        ),
    ]
