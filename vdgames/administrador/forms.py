from django import forms
from home.models import Colaboradores

from django.forms import ModelForm

class formuser(ModelForm):
    class Meta:
        model = Colaboradores
        fields = "__all__"