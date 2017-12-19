import csv
import os
from datetime import datetime

from celery.task import task
from celery.utils.log import get_task_logger
from django.conf import settings

from iptu.core.models import Iptu

logger = get_task_logger(__name__)


def generator_iptu_instance(data):
    for d in data:
        parametros = {
            'num_contrib': d['NUMERO DO CONTRIBUINTE'],
            'ano_exerc': d['ANO DO EXERCICIO'],
            'num_nl': d['NUMERO DA NL'],
            'data_cadastro': datetime.strptime(d['DATA DO CADASTRAMENTO'], '%d/%m/%y').date(),
            'tipo_contrib_1': d['TIPO DE CONTRIBUINTE 1'],
            'doc_contrib_1': d['CPF/CNPJ DO CONTRIBUINTE 1'],
            'nome_contrib_1': d['NOME DO CONTRIBUINTE 1'],
            'tipo_contrib_2': d['TIPO DE CONTRIBUINTE 2'],
            'doc_contrib_2': d['CPF/CNPJ DO CONTRIBUINTE 2'],
            'nome_contrib_2': d['NOME DO CONTRIBUINTE 2'],
            'num_condominio': d['NUMERO DO CONDOMINIO'],
            'codlog_imovel': d['CODLOG DO IMOVEL'],
            'logradouro_imovel': d['NOME DE LOGRADOURO DO IMOVEL'],
            'num_imovel': (0 if d['NUMERO DO IMOVEL'] == '' else int(d['NUMERO DO IMOVEL'])),
            'complemento_imovel': d['COMPLEMENTO DO IMOVEL'],
            'bairro_imovel': d['BAIRRO DO IMOVEL'],
            'ref_imovel': d['REFERENCIA DO IMOVEL'],
            'cep_imovel': d['CEP DO IMOVEL'],
            'esq_frente': d['QUANTIDADE DE ESQUINAS/FRENTES'],
            'fracao_ideal': float(d['FRACAO IDEAL'].replace(',', '.')),
            'area_terreno': d['AREA DO TERRENO'],
            'area_contruida': d['AREA CONSTRUIDA'],
            'area_ocupada': d['AREA OCUPADA'],
            'valor_m2_terreno': float(d['VALOR DO M2 DO TERRENO'].replace(',', '.')),
            'valor_m2_construido': float(d['VALOR DO M2 DE CONSTRUCAO'].replace(',', '.')),
            'ano_construcao': d['ANO DA CONSTRUCAO CORRIGIDO'],
            'qde_pavimentos': d['QUANTIDADE DE PAVIMENTOS'],
            'testada_calculo': float(d['TESTADA PARA CALCULO'].replace(',', '.')),
            'tipo_uso': d['TIPO DE USO DO IMOVEL'],
            'tipo_construcao': d['TIPO DE PADRAO DA CONSTRUCAO'],
            'tipo_terreno': d['TIPO DE TERRENO'],
            'fator_obsolencia': float(d['FATOR DE OBSOLESCENCIA'].replace(',', '.')),
            'ano_inicio_vida_contrib': d['ANO DE INICIO DA VIDA DO CONTRIBUINTE'],
            'mes_inicio_vida_contrib': d['MES DE INICIO DA VIDA DO CONTRIBUINTE'],
            'fase_contrib': d['FASE DO CONTRIBUINTE'],
        }
        yield Iptu(**parametros)


@task(name='create_db_iptu')
def create_db_iptu():
    data_file = os.path.join(settings.BASE_DIR, 'iptu', 'core', 'static', 'data', 'IPTU_2017.csv')
    with open(data_file, 'r', encoding='iso-8859-1') as file:
        rows = csv.DictReader(file, delimiter=';')
        fields = []
        contador = 0
        for iptu_instance in generator_iptu_instance(rows):
            fields.append(iptu_instance)
            contador += 1
            if contador == 100000:
                Iptu.objects.bulk_create(fields, batch_size=100000)
                del fields
                fields = []
                contador = 0
        if len(fields) > 0:
            Iptu.objects.bulk_create(fields)
