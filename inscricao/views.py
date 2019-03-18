from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import InscricaoForm, CandidatoForm
from django.contrib import messages
from .models import *


def home(request):
    e = Evento.objects.all()
    return render(request, 'home.html', {'evento': e})


@login_required
def dashboard(request):
    usuario = User.objects.get(pk=request.user.id)
    try:
        lista_candidato = Candidato.objects.get(usuario=usuario.id)
        return render(request, 'dashboard.html',
                      {'lista': lista_candidato})
    except Candidato.DoesNotExist:
        return redirect('inscricao:ficha_inscricao')


@login_required
def ficha_inscricao(request):
    form1 = CandidatoForm(request.POST, request.FILES)
    form2 = InscricaoForm(request.POST)
    # TODO Verificar o problema de inserir o candidato e não fazer a inscrição. Ou faz tudo ou não faz.

    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            candidato = form1.save(commit=False)
            candidato.usuario = request.user
            candidato.save()
            inscricao = form2.save(commit=False)
            inscricao.candidato = request.user.candidato
            inscricao.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('inscricao:comprovante_inscricao')
    return render(request, 'ficha_inscricao.html', {'form1': form1, 'form2': form2})


@login_required
def visualizar_cadastro(request):
    usuario = User.objects.get(pk=request.user.id)
    lista_candidato = Candidato.objects.get(usuario=usuario.id)
    return render(request, 'visualizar_cadastro.html', {'lista': lista_candidato})


@login_required
def comprovante_inscricao(request, pk):
    c = Candidato.objects.get(usuario=request.user)
# TODO Tem que receber o número da inscrição via POST
    i = Inscricao.objects.get(pk=pk)
    return render(request, 'comprovante_inscricao.html', {'i': i, 'c': c})
#    return render(request, 'comprovante_inscricao.html', {'i': i})


@login_required
def nova_inscricao(request):
    form = InscricaoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.candidato = request.user.candidato
            inscricao.save()
            messages.success(request, 'Inscrição confirmada no curso')
            url_comprovante = reverse_lazy('inscricao:comprovante_inscricao', kwargs={'pk': inscricao.pk})
            return redirect(url_comprovante)
    return render(request, 'nova_inscricao.html', {'form': form})
