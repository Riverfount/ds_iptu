# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171218_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iptu',
            name='qde_pavimentos',
            field=models.IntegerField(verbose_name='qde pavimentos'),
        ),
    ]
