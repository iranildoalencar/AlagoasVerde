from django.forms import ModelForm
from .models import Doadores

class DoadoresForm(ModelForm):
    class Meta:
        model = Doadores
        fields = ['first_name', 'last_name', 'bairro', 'cidade', 'estado', 'd_nasc']