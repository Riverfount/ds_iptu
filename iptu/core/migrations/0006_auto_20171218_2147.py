# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171218_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iptu',
            name='area_contruida',
            field=models.CharField(max_length=10, verbose_name='area construída'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='area_ocupada',
            field=models.CharField(max_length=10, verbose_name='area ocupada'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='area_terreno',
            field=models.CharField(max_length=10, verbose_name='area do terreno'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='data_cadastro',
            field=models.CharField(max_length=8, verbose_name='data cadastramento'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='esq_frente',
            field=models.CharField(max_length=3, verbose_name='nº esquina/frente'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='fase_contrib',
            field=models.CharField(max_length=2, verbose_name='fase contribuinte'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='fator_obsolencia',
            field=models.CharField(max_length=10, verbose_name='fator obsolencia'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='fracao_ideal',
            field=models.CharField(max_length=3, verbose_name='fração ideal'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='num_imovel',
            field=models.CharField(max_length=10, verbose_name='nº do imóvel'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='qde_pavimentos',
            field=models.CharField(max_length=50, verbose_name='qde pavimentos'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='testada_calculo',
            field=models.CharField(max_length=10, verbose_name='testada para cálculo'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='valor_m2_construido',
            field=models.CharField(max_length=10, verbose_name='valor m2 construído'),
        ),
        migrations.AlterField(
            model_name='iptu',
            name='valor_m2_terreno',
            field=models.CharField(max_length=10, verbose_name='valor m2 terreno'),
        ),
    ]
