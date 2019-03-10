from django.contrib import admin
from .models import Evento, Curso, Inscricao, Candidato

class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidato', 'evento', 'curso')

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'usuario', 'matricula')

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtd_vagas')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dta_inicio', 'dta_fim', 'situacao')


admin.site.register(Evento, EventoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
admin.site.register(Candidato, CandidatoAdmin)