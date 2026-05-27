from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura


class RegistroForm(UserCreationForm):

    ROLES = [
        ('administrador', 'Administrador'),
        ('cajero', 'Cajero'),
        ('mesero', 'Mesero'),
    ]

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ingrese su correo'
        })
    )

    rol = forms.ChoiceField(
        choices=ROLES,
        widget=forms.Select(attrs={
            'class': 'select-rol'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'rol', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese usuario'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingrese contraseña'
        })
    )

class ClienteForm(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = ['nombre', 'telefono', 'correo']

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'input'
            }),

            'telefono': forms.TextInput(attrs={
                'class': 'input'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'input'
            }),
        }

class EmpleadoForm(forms.ModelForm):

    class Meta:

        model = Empleado

        fields = ['nombre', 'telefono', 'correo', 'cargo']

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'input'
            }),

            'telefono': forms.TextInput(attrs={
                'class': 'input'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'input'
            }),

            'cargo': forms.TextInput(attrs={
                'class': 'input'
            }),
        }

class MesaForm(forms.ModelForm):

    class Meta:

        model = Mesa

        fields = ['numero_mesa', 'capacidad', 'estado_mesa']

        widgets = {

            'numero_mesa': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'capacidad': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'estado_mesa': forms.Select(attrs={
                'class': 'input'
            }),
        }

class PlatoForm(forms.ModelForm):

    class Meta:

        model = Plato

        fields = ['nombre_plato', 'descripcion', 'precio', 'categoria', 'disponible']

        widgets = {

            'nombre_plato': forms.TextInput(attrs={
                'class': 'input'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'input'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'categoria': forms.Select(attrs={
                'class': 'input'
            }),

            'disponible': forms.CheckboxInput(attrs={
                'class': 'input'
            }),
        }

class OrdenForm(forms.ModelForm):

    class Meta:

        model = Orden

        fields = ['cliente', 'empleado', 'mesa', 'estado_orden', 'total']

        widgets = {

            'cliente': forms.Select(attrs={
                'class': 'input'
            }),

            'empleado': forms.Select(attrs={
                'class': 'input'
            }),

            'mesa': forms.Select(attrs={
                'class': 'input'
            }),

            'estado_orden': forms.Select(attrs={
                'class': 'input'
            }),

            'total': forms.NumberInput(attrs={
                'class': 'input'
            }),
        }


class FacturaForm(forms.ModelForm):

    class Meta:

        model = Factura

        fields = ['orden', 'subtotal', 'impuesto', 'total_factura', 'metodo_pago']

        widgets = {

            'orden': forms.Select(attrs={
                'class': 'input'
            }),

            'subtotal': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'impuesto': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'total_factura': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'metodo_pago': forms.Select(attrs={
                'class': 'input'
            }),
        }