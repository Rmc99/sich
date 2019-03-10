from django.contrib import admin
from .models import Evento, Curso, Inscricao, Candidato

admin.site.register(Evento)
admin.site.register(Curso)
admin.site.register(Inscricao)
admin.site.register(Candidato)