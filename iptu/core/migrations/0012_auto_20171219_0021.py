# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171218_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iptu',
            name='ano_exerc',
            field=models.CharField(max_length=4, verbose_name='ano exercício'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='data_cadastro',
            field=models.DateField(verbose_name='data cadastramento'),
        ),
    ]
