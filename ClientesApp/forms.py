from django import forms
from LoginApp.models import Usuarios
from ClientesApp.models import Clientes


class AddUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class RegistarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['usuario', 'clave', 'estado']

class ClientesFrom(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'ci': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': '0905020810',
                    'id': 'cedula',
                    'name': 'cedula',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'John Doe',
                    'id': 'nombre',
                    'name': 'nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Peréz',
                    'id': 'apellido',
                    'name': 'apellido',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Guayaquil',
                    'id': 'direccion',
                    'name': 'direccion',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': '0958933521',
                    'id': 'telefono',
                    'name': 'telefono',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'example@hotmail.com',
                    'id': 'correo',
                    'name': 'correo',
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Ecuatoriano',
                    'id': 'nacionalidad',
                    'name': 'nacionalidad',
                }
            ),
            'estado_Civil': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Soltero',
                    'id': 'estado',
                    'name': 'estado',
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'formulario__checkbox',
                    'id': 'terminos',
                    'name': 'terminos',
                }
            ),
        }