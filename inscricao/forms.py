from django.forms import ModelForm
from .models import Inscricao, Candidato

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = "__all__"

class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = "__all__"