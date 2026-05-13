from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClienteForm, EmpleadoForm, MesaForm, PlatoForm, OrdenForm, FacturaForm

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
 
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'gestion/clientes.html',{'clientes': clientes})

@login_required
def crear_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('clientes')

    else:

        form = ClienteForm()

    return render(
        request,
        'gestion/crear_cliente.html',
        {
            'form': form
        }
    )

@login_required
def editar_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    if request.method == 'POST':

        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():

            form.save()

            return redirect('clientes')

    else:

        form = ClienteForm(instance=cliente)

    return render(
        request,
        'gestion/editar_cliente.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    cliente.delete()

    return redirect('clientes')
 

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})

@login_required
def crear_empleado(request):
    if request.method == 'POST':

        form = EmpleadoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('empleados')

    else:

        form = EmpleadoForm()

    return render(
        request,
        'gestion/crear_empleado.html',
        {
            'form': form
        }
    )

@login_required
def editar_empleado(request, id):

    empleado = get_object_or_404(
        Empleado,
        id=id
    )

    if request.method == 'POST':

        form = EmpleadoForm(
            request.POST,
            instance=empleado
        )

        if form.is_valid():

            form.save()

            return redirect('empleados')

    else:

        form = EmpleadoForm(instance=empleado)

    return render(
        request,
        'gestion/editar_empleado.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_empleado(request, id):

    empleado = get_object_or_404(
        Empleado,
        id=id
    )

    empleado.delete()

    return redirect('empleados')
 

@login_required
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})

@login_required
def crear_mesa(request):
    if request.method == 'POST':

        form = MesaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('mesas')

    else:

        form = MesaForm()

    return render(
        request,
        'gestion/crear_mesa.html',
        {
            'form': form
        }
    )

@login_required
def editar_mesa(request, id):

    mesa = get_object_or_404(
        Mesa,
        id=id
    )

    if request.method == 'POST':

        form = MesaForm(
            request.POST,
            instance=mesa
        )

        if form.is_valid():

            form.save()

            return redirect('mesas')

    else:

        form = MesaForm(instance=mesa)

    return render(
        request,
        'gestion/editar_mesa.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_mesa(request, id):

    mesa = get_object_or_404(
        Mesa,
        id=id
    )

    mesa.delete()

    return redirect('mesas')
 

@login_required
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})

@login_required
def crear_plato(request):
    if request.method == 'POST':

        form = PlatoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('platos')

    else:

        form = PlatoForm()

    return render(
        request,
        'gestion/crear_plato.html',
        {
            'form': form
        }
    )

@login_required
def editar_plato(request, id):

    plato = get_object_or_404(
        Plato,
        id=id
    )

    if request.method == 'POST':

        form = PlatoForm(
            request.POST,
            instance=plato
        )

        if form.is_valid():

            form.save()

            return redirect('platos')

    else:

        form = PlatoForm(instance=plato)

    return render(
        request,
        'gestion/editar_plato.html',
        {
            'form': form
        }
    )


@login_required
def eliminar_plato(request, id):

    plato = get_object_or_404(
        Plato,
        id=id
    )

    plato.delete()

    return redirect('platos')

@login_required
def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})
 
@login_required
def crear_orden(request):
    if request.method == 'POST':

        form = OrdenForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('ordenes')

    else:

        form = OrdenForm()

    return render(
        request,
        'gestion/crear_orden.html',
        {
            'form': form
        }
    )

@login_required
def editar_orden(request, id):

    orden = get_object_or_404(
        Orden,
        id=id
    )

    if request.method == 'POST':

        form = OrdenForm(
            request.POST,
            instance=orden
        )

        if form.is_valid():

            form.save()

            return redirect('ordenes')

    else:

        form = OrdenForm(instance=orden)

    return render(
        request,
        'gestion/editar_orden.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_orden(request, id):

    orden = get_object_or_404(
        Orden,
        id=id
    )

    orden.delete()

    return redirect('ordenes')

@login_required
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})

@login_required
def crear_factura(request):
    if request.method == 'POST':

        form = FacturaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('facturas')

    else:

        form = FacturaForm()

    return render(
        request,
        'gestion/crear_factura.html',
        {
            'form': form
        }
    )

@login_required
def editar_factura(request, id):

    factura = get_object_or_404(
        Factura,
        id=id
    )

    if request.method == 'POST':

        form = FacturaForm(
            request.POST,
            instance=factura
        )

        if form.is_valid():

            form.save()

            return redirect('facturas')

    else:

        form = FacturaForm(instance=factura)

    return render(
        request,
        'gestion/editar_factura.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_factura(request, id):

    factura = get_object_or_404(
        Factura,
        id=id
    )

    factura.delete()

    return redirect('facturas')

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
    return redirect('/login/')


# DASHBOARD
@login_required
def dashboard(request):
    return render(request, 'gestion/dashboard.html')