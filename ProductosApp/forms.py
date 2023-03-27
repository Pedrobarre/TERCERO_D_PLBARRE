from django import forms
from django.forms import widgets

from ProductosApp.models import Productos


class RegistarProductos(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'






