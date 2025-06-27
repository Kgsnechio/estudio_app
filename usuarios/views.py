from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroUserForms

from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(request):

    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logado com sucesso.')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return redirect('login')

    return render(request, 'usuarios/login.html', { 'form': form })

def cadastro(request):

    form = CadastroUserForms()

    if request.method == 'POST':
        form = CadastroUserForms(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, 'Novo usuário cadastrado com sucesso.')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', { 'form': form })

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso.')
    print('DESLOGOU AQUI')
    return redirect('login')
