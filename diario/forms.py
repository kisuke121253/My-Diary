from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Informe um endereço de email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import AcompanhamentoSemanal