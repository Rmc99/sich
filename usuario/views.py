from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterForm

User = get_user_model()

def registrar(request):
    template_name = 'registrar.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('inscricao:ficha_inscricao')
    else:
        form = RegisterForm()

    context = {'form': form }
    return render(request, template_name, context)