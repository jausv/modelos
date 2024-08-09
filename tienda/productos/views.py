from django.shortcuts import render
from .models import Cliente
from . models import Producto

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_productos(request):
    Productos = Producto.objects.all()
    return render(request, 'listar_productos.html',{'productos':Productos})
