from django.forms import ModelForm
from .models import Inscricao, Candidato
from django import forms


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        exclude = ['usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'dta_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        exclude = ['candidato']

        widgets = {
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }