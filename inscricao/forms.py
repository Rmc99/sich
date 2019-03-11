from django.forms import ModelForm
from .models import Inscricao, Candidato

class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        exclude = ['usuario']

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        exclude = ['candidato']