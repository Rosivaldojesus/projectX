# Generated by Django 3.0 on 2021-04-19 16:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210419_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 16, 7, 56, 893395, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150)),
                ('email_comentario', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(default=datetime.datetime(2021, 4, 19, 16, 7, 56, 897391, tzinfo=utc))),
                ('publicado_comentario', models.BooleanField(default=False)),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('usuario_comentario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comentário',
            },
        ),
    ]
