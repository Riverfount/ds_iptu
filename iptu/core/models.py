from django.db import models
from djmoney.models.fields import MoneyField


class Iptu(models.Model):
    num_contrib = models.CharField('nº contribuinte', max_length=12, unique=True, primary_key=True, db_index=True)
    ano_exerc = models.CharField('ano exercício', max_length=4)
    num_nl = models.CharField('num. nl', max_length=1)
    data_cadastro = models.DateField('data cadastramento')
    tipo_contrib_1 = models.CharField('Tipo contribuinte 1', max_length=22)
    doc_contrib_1 = models.CharField('CPF/CNPJ contribuinte 1', max_length=14)
    nome_contrib_1 = models.CharField('nome contribuinte', max_length=255)
    tipo_contrib_2 = models.CharField('Tipo Contribuinte 2', max_length=22, blank=True)
    doc_contrib_2 = models.CharField('CPF/CNPJ contribuinte 2', max_length=14, blank=True)
    nome_contrib_2 = models.CharField('nome contribuinte 2', max_length=255, blank=True)
    num_condominio = models.CharField('nº condomínio', max_length=10)
    codlog_imovel = models.CharField('CODLOG do imóvel', max_length=10)
    logradouro_imovel = models.CharField('logradouro imóvel', max_length=255)
    num_imovel = models.IntegerField('nº do imóvel')
    complemento_imovel = models.CharField('complemento', max_length=255, blank=True)
    bairro_imovel = models.CharField('bairro', max_length=255, blank=True)
    ref_imovel = models.CharField('referência', max_length=255, blank=True)
    cep_imovel = models.CharField('CEP', max_length=9)
    esq_frente = models.IntegerField('nº esquina/frente')
    fracao_ideal = models.FloatField('fração ideal')
    area_terreno = models.IntegerField('area do terreno')
    area_contruida = models.IntegerField('area construída')
    area_ocupada = models.IntegerField('area ocupada')
    valor_m2_terreno = MoneyField('valor m2 terreno', max_digits=10, decimal_places=2, default_currency='BRL')
    valor_m2_construido = MoneyField('valor m2 construído', max_digits=10, decimal_places=2, default_currency='BRL')
    ano_construcao = models.CharField('ano construção', max_length=4)
    qde_pavimentos = models.IntegerField('qde pavimentos')
    testada_calculo = models.FloatField('testada para cálculo')
    tipo_uso = models.CharField('tipo uso', max_length=255)
    tipo_construcao = models.CharField('tipo padrão construção', max_length=255)
    tipo_terreno = models.CharField('tipo terreno', max_length=255)
    fator_obsolencia = models.FloatField('fator obsolencia')
    ano_inicio_vida_contrib = models.CharField('ano início vida contribuinte', max_length=4)
    mes_inicio_vida_contrib = models.CharField('mês início vida contribuinte', max_length=2)
    fase_contrib = models.IntegerField('fase contribuinte')

    class Meta:
        verbose_name = 'IPTU 2017'
        verbose_name_plural = 'IPTU 2017'
        ordering = ['num_contrib']

    def __str__(self):
        return self.num_contrib

    def valor_imovel(self):
        valor = (self.valor_m2_terreno * self.area_terreno) + (self.valor_m2_construido * self.area_contruida)
        return valor
