from django.forms import ModelForm
from django import forms
from .models import Pedido
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")