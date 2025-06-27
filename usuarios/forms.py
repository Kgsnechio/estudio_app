from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuario', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}))
    password = forms.CharField(label='Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))

class CadastroUserForms(forms.Form):
    username = forms.CharField(label='Usuário', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
    password = forms.CharField(label='Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))
    password2 = forms.CharField(label='Confirmar Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Senhas diferentes.')

        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('Email ja cadastrado.')

        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            username = username.strip()

            if " " in username:
                raise ValidationError('Não pode conter espaços no nome de usuário.')

            if len(username) < 5:
                raise ValidationError('Nome de usuário muito curto. No mínimo 5 caracteres.')

            if User.objects.filter(username=username).exists():
                raise ValidationError('Nome de usuário ja cadastrado.')

        return username
