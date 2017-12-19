from django.contrib import admin

from iptu.core.models import Iptu


class IptuModelAdmin(admin.ModelAdmin):
    list_display = ['num_contrib', 'nome_contrib_1', 'logradouro_imovel', 'num_imovel', 'cep_imovel', 'valor_imovel']
    search_fields = ['num_contrib', 'nome_contrib_1', 'codlog_imovel',
                     'logradouro_imovel', 'bairro_imovel', 'cep_imovel']
    ordering = ['num_contrib']


admin.site.register(Iptu, IptuModelAdmin)
