from django.test import TestCase
from iptu.core.models import Iptu
from datetime import datetime


class IptuModelTest(TestCase):
    def setUp(self):
        self.iptu = Iptu.objects.create(
            num_contrib='0010030003-0', ano_exerc='2017', num_nl='1',
            data_cadastro=datetime.strptime('14/01/17', '%d/%m/%y').date(),
            tipo_contrib_1='PESSOA FISICA (CPF)', doc_contrib_1='XXXXXX0214XXXX', nome_contrib_1='MARCIO MOURCHED',
            tipo_contrib_2='', doc_contrib_2='', nome_contrib_2='', num_condominio='00-0', codlog_imovel='03812-1',
            logradouro_imovel='R S CAETANO', num_imovel=13, complemento_imovel='', bairro_imovel='SANTA EFIGENIA',
            ref_imovel='', cep_imovel='01104-001', esq_frente=1, fracao_ideal=float('1.0000'.replace(',', '.')),
            area_terreno=136, area_contruida=135, area_ocupada=108, valor_m2_terreno=float('2103,00'.replace(',', '.')),
            valor_m2_construido=float('1566,00'.replace(',', '.')), ano_construcao='1924', qde_pavimentos=1,
            testada_calculo=float('13,00'.replace(',', '.')), tipo_uso='Loja',
            tipo_construcao='Comercial horizontal - padrão B', tipo_terreno='De esquina',
            fator_obsolencia=float('0,20'.replace(',', '.')), ano_inicio_vida_contrib='1963',
            mes_inicio_vida_contrib='1', fase_contrib=0, )

    def test_create(self):
        self.assertTrue(Iptu.objects.exists())

    def test_tipo_contribe_2_can_be_blank(self):
        field = Iptu._meta.get_field('tipo_contrib_2')
        self.assertTrue(field.blank)

    def test_doc_contrib_2_can_be_blank(self):
        field = Iptu._meta.get_field('doc_contrib_2')
        self.assertTrue(field.blank)

    def test_nome_contrib_2_can_be_blank(self):
        field = Iptu._meta.get_field('nome_contrib_2')
        self.assertTrue(field.blank)

    def test_complemento_imovel_can_be_blank(self):
        field = Iptu._meta.get_field('complemento_imovel')
        self.assertTrue(field.blank)

    def test_bairro_imovel_can_be_blank(self):
        field = Iptu._meta.get_field('bairro_imovel')
        self.assertTrue(field.blank)

    def test_ref_imovel_can_be_blank(self):
        field = Iptu._meta.get_field('complemento_imovel')
        self.assertTrue(field.blank)
