from django import forms
from models import Usuarios

from django.forms import ModelForm

class formuser(ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"