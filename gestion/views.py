from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura

@login_required
def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas': Mesa.objects.count(),
        'total_platos': Plato.objects.count(),
        'total_ordenes': Orden.objects.count(),
        'total_facturas': Factura.objects.count()
    }
    return render(request, 'gestion/inicio.html', context)
 

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})
 

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})
 

def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})
 

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})
 

def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})
 

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})

# REGISTRO
def registro_view(request):

    if request.method == 'POST':

        form = RegistroForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Usuario registrado correctamente'
            )

            return redirect('login')

    else:
        form = RegistroForm()

    return render(
        request,
        'gestion/registro.html',
        {'form': form}
    )


# LOGIN
def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    else:
        messages.error(
                request,
                'Usuario o contraseña incorrectos'
            )
        form = LoginForm()

    return render(request, 'gestion/login.html', {'form': form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD
@login_required
def dashboard(request):
    return render(request, 'gestion/dashboard.html')