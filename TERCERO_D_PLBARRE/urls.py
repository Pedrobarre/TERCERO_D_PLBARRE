"""TERCERO_D_PLBARRE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from LoginApp.views import login_requierd,LoginSeccion,salir,RegistrarUsuario,dashobord
from ClientesApp.views import listUsuarios,CrearUsuario,EditarUsuario,EliminarUsuario,\
    RegistrarCliente,listClientes,EditarCliente,EliminarCliente
from ProductosApp.views import listProductos,EliminarProducto,CrearProducto,EditarProducto

urlpatterns = [
    path('', login_requierd),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginSeccion, name='login'),
    path('salir/', salir, name='salir'),
    path('listProductos/', listProductos, name='listProductos'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashobord, name='dashboard'),
    path('RegistrarUsuario/', RegistrarUsuario, name='RegistrarUsuario'),
    path('RegistrarCliente/', RegistrarCliente, name='RegistrarCliente'),
    path('listUsuarios/', listUsuarios, name='listUsuarios'),
    path('listClientes/', listClientes, name='listado_clientes'),
    path('CrearUsuario/', CrearUsuario, name='CrearUsuario'),
    path('editar_usuario/<int:id>', EditarUsuario, name='editar_usuario'),
    path('EditarCliente/<int:id>', EditarCliente, name='EditarCliente'),
    path('eliminar_usuario/<int:id>', EliminarUsuario, name='eliminar_usuario'),
    path('EliminarCliente/<int:id>', EliminarCliente, name='EliminarCliente'),
    path('RegistarProducto/', CrearProducto, name='RegistarProductos'),
    path('listProductos/', listProductos, name='listProductos'),
    path('EliminarProducto/<int:id>', EliminarProducto, name='EliminarProducto'),
    path('EditarProducto/<int:id>', EditarProducto, name='EditarProducto'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
