from django import forms
from .models import Colaboradores

from django.forms import ModelForm

class formuser(ModelForm):
    class Meta:
        model = Colaboradores
        fields = "__all__"

class loginforms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)