from django.shortcuts import render, redirect
from .forms import InscricaoForm, CandidatoForm
from django.contrib import messages

def ficha_inscricao(request):
    f = CandidatoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if f.is_valid():
            candidato = f.save(commit=False)
            candidato.usuario = request.user
            candidato.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('inscricao:ficha_inscricao')

    form = InscricaoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.usuario = request.user
            inscricao.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('inscricao:ficha_inscricao')
    return render(request, 'ficha_inscricao.html', {'form': form, 'f': f})
