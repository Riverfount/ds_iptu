# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20171219_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iptu',
            name='num_contrib',
            field=models.CharField(db_index=True, max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='nº contribuinte'),
        ),
    ]
