from django.shortcuts import render,redirect
from ProductosApp.models import Productos
from ProductosApp.forms import RegistarProductos
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def listProductos(request):
    queryset = request.GET.get("busqueda")
    producto = Productos.objects.all()
    if queryset:
        producto = Productos.objects.filter(
            Q(producto__icontains = queryset)
        ).distinct()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(producto, 3)
        producto = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': producto,
        'paginator': paginator,
    }
    return render(request, 'listProductos.html', context)
def CrearProducto(request):
    if request.method == 'POST':
        productofrom = RegistarProductos(request.POST)
        if productofrom.is_valid():
            productofrom.save()
            return redirect('listProductos')
    else:
        productofrom =RegistarProductos()
    return render(request, 'crearProductos.html', {'productofrom': productofrom})
#<-- editar usuario -->
def EditarProducto(request,id):
    producto = Productos.objects.get(id = id)
    if request.method == 'GET':
        productofrom = RegistarProductos(instance= producto)
    else:
        productofrom = RegistarProductos(request.POST, instance= producto)
        if productofrom.is_valid():
            productofrom.save()
        return redirect('listProductos')
    return render(request, 'editarProducto.html', {'productofrom':productofrom})
#<-- eliminar usuario -->
def EliminarProducto(request,id):
    producto = Productos.objects.get(id = id)
    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('listProductos')
    return render(request,'eliminarProducto.html',{'producto': producto})
