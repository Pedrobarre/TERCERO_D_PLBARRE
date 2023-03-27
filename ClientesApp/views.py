from django.shortcuts import render,redirect
from LoginApp.models import Usuarios
from ClientesApp.models import Clientes
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
from ClientesApp.forms import AddUsuarioForm,EditarUsuarioForm,ClientesFrom

# Create your views here.

def listUsuarios(request):
    queryset = request.GET.get("busqueda")
    usuario = Usuarios.objects.all()
    if queryset:
        usuario = Usuarios.objects.filter(
            Q(nombres__icontains = queryset) |
            Q(usuario__icontains = queryset)
        ).distinct()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(usuario, 3)
        usuario = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': usuario,
        'paginator': paginator,
    }
    return render(request, 'listUsuarios.html', context )
#<-- crear usuario -->
def CrearUsuario(request):
    if request.method == 'POST':
        createform = AddUsuarioForm(request.POST)
        if createform.is_valid():
            createform.save()
            return redirect('listUsuarios')
    else:
        createform =AddUsuarioForm()
    return render(request, 'crearUsuario.html', {'createform': createform})
#<-- editar usuario -->
def EditarUsuario(request,id):
    usuario = Usuarios.objects.get(id = id)
    if request.method == 'GET':
        createform = EditarUsuarioForm(instance= usuario)
    else:
        createform = EditarUsuarioForm(request.POST, instance= usuario)
        if createform.is_valid():
            createform.save()
        return redirect('listUsuarios')
    return render(request, 'editarUsuario.html', {'createform':createform})
#<-- eliminar usuario -->
def EliminarUsuario(request,id):
    usuario = Usuarios.objects.get(id = id)
    if request.method == 'POST':
        usuario.estado = False
        usuario.save()
        return redirect('listUsuarios')
    return render(request,'eliminarUsuario.html',{'usuario': usuario})
#<-- listar Clientes -->
def listClientes(request):
    queryset = request.GET.get("busqueda")
    cliente = Clientes.objects.all()
    if queryset:
        cliente = Clientes.objects.filter(
            Q(ci__icontains=queryset) |
            Q(apellido__icontains=queryset)|
            Q(apellido__icontains=queryset)
        ).distinct()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(cliente, 3)
        cliente = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': cliente,
        'paginator': paginator,
    }
    return render(request, 'listaClientes.html', context)
#<-- Rwgistrar Clientes -->
def RegistrarCliente(request):
    if request.method == 'POST':
        createform = ClientesFrom(request.POST)
        if createform.is_valid():
            createform.save()
            return redirect('listado_clientes')
    else:
        createform =ClientesFrom()
    return render(request, 'crearClientes.html', {'createform': createform})
#<-- editar Clientes -->
def EditarCliente(request,id):
    cliente = Clientes.objects.get(id = id)
    if request.method == 'GET':
        createform = ClientesFrom(instance= cliente)
    else:
        createform = ClientesFrom(request.POST, instance= cliente)
        if createform.is_valid():
            createform.save()
        return redirect('listado_clientes')
    return render(request, 'editarClientes.html', {'createform':createform})
#<-- eliminar Clientes -->
def EliminarCliente(request,id):
    cliente = Clientes.objects.get(id = id)
    if request.method == 'POST':
        cliente.estado = False
        cliente.save()
        return redirect('listado_clientes')
    return render(request,'elimarClientes.html',{'cliente': cliente})
