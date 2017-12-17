# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_produto', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('grupos', models.CharField(max_length=255)),
                ('codigo_barras', models.PositiveIntegerField(default=0)),
                ('unidade', models.CharField(max_length=2)),
                ('peso', models.FloatField(default=0)),
                ('estoque', models.PositiveIntegerField(default=0)),
                ('valor', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
