from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from LoginApp.models import Usuarios
from ClientesApp.models import Clientes
from ProductosApp.models import Productos,Distribuiodra


# Create your views here.

#<-- requerir seccion -->
@login_required()
def login_requierd(request):
    return render(request, 'registration/login.html')
#<-- ingresar seccion -->
def LoginSeccion(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {})
    else:
        Username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usuario = Usuarios.objects.get(usuario=Username, clave=password)
            return render(request, "index.html", {"Username": usuario.usuario})
        except Usuarios.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectas')
            return render(request, "registration/login.html",{})
#<-- salir seccion -->
def salir(request):
    logout(request)
    return redirect('login')
#<!--- regsitro de usuario -->
def RegistrarUsuario(request):
   nombres=request.POST['txtnombre']
   correo = request.POST['txtcorreo']
   usuario = request.POST['txtusaurio']
   clave = request.POST['txtcontrraseña']

   usuario1 = Usuarios.objects.create(nombres=nombres, correo=correo, usuario=usuario, clave=clave)
   return redirect('login')
#<!--- regsitro de usuario -->
def dashobord(request):
    distribuioda = Distribuiodra.objects.filter(estado=True)
    producto = Productos.objects.filter(estado=True)
    producto_agotado = Productos.objects.filter(estado=False)
    cliente = Clientes.objects.filter(estado=True)
    usuario = Usuarios.objects.filter(estado=True)
    total_cliente = cliente.count()
    total_producto = producto.count()
    total_producto_agotado = producto_agotado.count()
    total_usuarios = usuario.count()
    total_distribuidora = distribuioda.count()
    context = {
        'total_usuarios': total_usuarios,
        'total_distribuidora': total_distribuidora,
        'total_cliente': total_cliente,
        'total_producto': total_producto,
        'total_producto_agotado': total_producto_agotado,
    }
    return render(request, 'dashboard.html', context)