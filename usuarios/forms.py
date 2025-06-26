from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuario', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}))
    password = forms.CharField(label='Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))

class CadastroUserForms(forms.Form):
    username = forms.CharField(label='Usuário', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
    password = forms.CharField(label='Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))
    password2 = forms.CharField(label='Confirmar Senha', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}))