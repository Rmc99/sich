from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import InscricaoForm, CandidatoForm
from django.contrib import messages
from .models import *

@login_required
def ficha_inscricao(request):
    form1 = CandidatoForm(request.POST, request.FILES)
    form2 = InscricaoForm(request.POST)
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            candidato = form1.save(commit=False)
            inscricao = form2.save(commit=False)
            inscricao.candidato = request.user.candidato
            candidato.usuario = request.user
            inscricao.save()
            candidato.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('inscricao:home')
    return render(request, 'ficha_inscricao.html', {'form1': form1, 'form2': form2})

def home(request):
    e = Evento.objects.all()
    return render(request, 'home.html', {'evento': e})