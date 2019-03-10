import csv
import io
from django.http import StreamingHttpResponse
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from .models import *
from django.forms import TextInput
from django.db import models
from decimal import Decimal, InvalidOperation

class PagamentoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pessoa']
    list_display = ('ano', 'mes', 'pessoa', 'categoria', 'funcao', 'valor_bruto', 'valor_irpf', 'valor_liquido')
    search_fields = ['ano', 'mes', 'categoria', 'funcao', 'pessoa__nome']
    fieldsets = (
        ('Dados do Pagamento:', {'fields': (('ano', 'mes', 'pessoa'), ('categoria', 'funcao', 'qtd_horas'),
         ('valor_hora', 'valor_pensao'), ('qtd_dependente_irpf', 'outras_deducoes'))}),
        ('Calculos:', {'fields': (('valor_bruto', 'valor_inss',
             'valor_iss'), ('deducao_irpf', 'valor_pos_deducao_irpf', 'valor_irpf'), ('valor_liquido', 'valor_patronal'))}),
    )
    list_filter = ('ano', 'mes', 'categoria', 'funcao', 'pessoa__nome')

#    readonly_fields = ('valor_bruto', 'valor_inss', 'valor_iss', 'deducao_irpf', 'valor_pos_deducao_irpf', 'valor_irpf',
#                       'valor_liquido', 'valor_patronal')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        model = self.model
        output = io.StringIO()

        model_fields = [field.name for field in model._meta.fields]
        extra_fields = ['email', 'telefone', 'cpf', 'pis', 'num_conta', 'num_agencia', 'num_operacao', 'num_banco']
        fieldnames = model_fields + extra_fields
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for obj in queryset:
            obj_values = {field: getattr(obj, field) for field in model_fields}
            obj_values['email'] = obj.pessoa.email
            obj_values['telefone'] = obj.pessoa.telefone
            obj_values['cpf'] = obj.pessoa.cpf
            obj_values['pis'] = obj.pessoa.pis
            obj_values['num_conta'] = obj.pessoa.num_conta
            obj_values['num_agencia'] = obj.pessoa.num_agencia
            obj_values['num_operacao'] = obj.pessoa.num_operacao
            obj_values['num_banco'] = obj.pessoa.num_banco

            writer.writerow(obj_values)

        response = StreamingHttpResponse(output.getvalue(),
                                         content_type='text/csv')
        disposition = 'attachment; filename="relatorio_pagamento.csv"'
        response['Content-Disposition'] = disposition
        response['mimetype'] = "text/csv"
        return response
    export_as_csv.short_description = "Exportar Selecionados"

# exibir o cpf no list_display
#    def get_cpf(self, obj):
#        return obj.pessoa.cpf
#   get_cpf.short_description = 'CPF'

    def response_change(self, request, obj):
        self.calcular(obj)
        try:
            obj.save()
            return super().response_change(request, obj)
        except InvalidOperation:
            redirect_url = request.path
            messages.error(request, 'ERRO! Verifique se os dados inseridos estão corretos!')
            return HttpResponseRedirect(redirect_url)

    def response_add(self, request, obj):
        self.calcular(obj)
        try:
            obj.save()
            return super().response_add(request, obj)
        except InvalidOperation:
            redirect_url = request.path
            messages.error(request, 'ERRO! Verifique se os dados inseridos estão corretos!')
            return HttpResponseRedirect(redirect_url)

    def calcular(self, obj):
        tx_iss = Decimal(0.05)
        tx_patronal = Decimal(0.20)
        tx_por_dependente = Decimal(189.59)
        tx_inss = Decimal(0.11)
        aliquota_1 = Decimal(0.075)
        parc_deduzir_1 = Decimal(142.80)
        aliquota_2 = Decimal(0.15)
        parc_deduzir_2 = Decimal(354.80)
        aliquota_3 = Decimal(0.225)
        parc_deduzir_3 = Decimal(636.13)
        aliquota_4 = Decimal(0.275)
        parc_deduzir_4 = Decimal(869.36)

        # calculo do valor bruto
        obj.valor_bruto = (obj.qtd_horas * obj.valor_hora)
        # calculo inss 11%
        obj.valor_inss = (obj.valor_bruto * tx_inss)
        # calculo 5% iss
        obj.valor_iss = (obj.valor_bruto * tx_iss)
        # calculo 20% patronal
        obj.valor_patronal = (obj.valor_bruto * tx_patronal)
        # calculo valor por dependente
        valor_total_por_dependente = Decimal(obj.qtd_dependente_irpf * tx_por_dependente)

        # calculo deducoes irpf
        obj.deducao_irpf = (obj.valor_inss + obj.valor_pensao + valor_total_por_dependente + obj.outras_deducoes);
        # calculo pos deducao irpf
        obj.valor_pos_deducao_irpf = (obj.valor_bruto - obj.valor_inss - obj.valor_pensao - valor_total_por_dependente - obj.outras_deducoes)

        # calculos para colaborador/professor interno do ifma/colun
        if (obj.categoria == 1 or obj.categoria == 3):
            obj.valor_liquido = obj.valor_bruto
            obj.valor_inss = 0
            obj.valor_iss = 0
            obj.deducao_irpf = 0
            obj.valor_irpf = 0
            obj.valor_pos_deducao_irpf = 0
            obj.valor_patronal = 0
        # isento de irpf
        elif (obj.valor_pos_deducao_irpf <= 1903.98):
            obj.valor_irpf = 0
            obj.deducao_irpf = 0
            obj.valor_irpf = 0
            obj.valor_pos_deducao_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss)
        # aliquota de 7,5%
        elif (obj.valor_pos_deducao_irpf >= 1903.99 and obj.valor_pos_deducao_irpf <= 2826.65):
            obj.valor_irpf = (obj.valor_bruto - valor_total_por_dependente - obj.valor_inss - obj.valor_pensao - obj.outras_deducoes) * aliquota_1 - parc_deduzir_1
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (obj.valor_pos_deducao_irpf >= 2826.66 and obj.valor_pos_deducao_irpf <= 3751.05):
            obj.valor_irpf = (obj.valor_bruto - valor_total_por_dependente - obj.valor_inss - obj.valor_pensao - obj.outras_deducoes) * aliquota_2 - parc_deduzir_2
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (obj.valor_pos_deducao_irpf >= 3751.06 and obj.valor_pos_deducao_irpf <= 4664.68):
            obj.valor_irpf = (obj.valor_bruto - valor_total_por_dependente - obj.valor_inss - obj.valor_pensao - obj.outras_deducoes) * aliquota_3 - parc_deduzir_3
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        elif (obj.valor_pos_deducao_irpf > 4664.68):
            obj.valor_irpf = (obj.valor_bruto - valor_total_por_dependente - obj.valor_inss - obj.valor_pensao - obj.outras_deducoes) * aliquota_4 - parc_deduzir_4
            if (obj.valor_irpf <=0):
                obj.valor_irpf = 0
            obj.valor_liquido = (obj.valor_bruto - obj.valor_inss - obj.valor_iss - obj.valor_irpf)
        return (obj)

    class Media:
        js = (
            'js/pagamento/jquery-3.3.1.min.js',
            'js/pagamento/jquery.mask.min.js',
            'js/pagamento/jquery-mymask-pagamento.js',
        )

    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.DecimalField: {'widget': TextInput(attrs={'autocomplete': 'off'})},

    }

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf')
    list_display = ('nome', 'email', 'telefone', 'cpf', 'pis', 'num_conta', 'num_agencia', 'num_operacao', 'num_banco')
    #fields = ('nome', 'email', 'cpf', 'pis', 'num_conta', 'num_agencia', 'num_operacao', 'num_banco')
    fieldsets = (
        ('Dados Pessoais:', {'fields': (('nome', 'email'), ('telefone', 'cpf'), 'pis')}),
        ('Dados Bancários:', {'fields': (('num_conta', 'num_agencia'), ('num_operacao', 'num_banco'))}),
    )
    class Media:
        js = (
            'js/pessoa/jquery-3.3.1.min.js',
            'js/pessoa/jquery.mask.min.js',
            'js/pessoa/jquery-mymask.js',
        )
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
