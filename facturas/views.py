from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ClienteForm, ProductoForm
from facturas.models import Producto, Factura, Cliente
from django.contrib.auth.decorators import login_required

@login_required
def factura_nueva(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = Cliente.objects.create(
            nit = formulario.cleaned_data['nit'],
            nombre = formulario.cleaned_data['nombre'],
            apellido = formulario.cleaned_data['apellido'],
            direccion = formulario.cleaned_data['direccion'],
            email = formulario.cleaned_data['email'],
            telefono = formulario.cleaned_data['telefono'])
            for producto_id in request.POST.getlist('productos'):
                factura = Factura(producto_id=producto_id, cliente_id = cliente.id)
                factura.save()
            messages.add_message(request, messages.SUCCESS, 'Factura Creada con Exito.')
    else:
        formulario = ClienteForm()
    return render(request, 'facturas/factura_nueva.html', {'formulario': formulario})

@login_required
def factura_lista(request):
    #clientes = Factura.objects.filter(cliente__nit=12345678)
    clientes = Cliente.objects.all()
    return render(request, 'facturas/factura_lista.html', {'clientes': clientes})

@login_required
def factura_remove(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('factura_lista')

@login_required
def producto_lista(request):
    #clientes = Factura.objects.filter(cliente__nit=12345678)
    productos = Producto.objects.all()
    return render(request, 'productos/producto_lista.html', {'productos': productos})

@login_required
def producto_nuevo(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            producto = Producto.objects.create(
            nombre = formulario.cleaned_data['nombre'],
            precio = formulario.cleaned_data['precio'],
            stock = formulario.cleaned_data['stock'])
            return redirect('producto_lista')
            messages.add_message(request, messages.SUCCESS, 'Factura Creada con Exito.')
    else:
        formulario = ProductoForm()
    return render(request, 'productos/producto_crear.html', {'formulario': formulario})

@login_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            producto = formulario.save()
            producto.save()
            return redirect('producto_lista')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'productos/producto_editar.html', {'formulario': formulario})

@login_required
def producto_remove(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('producto_lista')
