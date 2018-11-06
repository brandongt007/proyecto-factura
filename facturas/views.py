from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ClienteForm
from facturas.models import Producto, Factura, Cliente

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

def factura_lista(request):
    #clientes = Factura.objects.filter(cliente__nit=12345678)
    clientes = Cliente.objects.all()
    return render(request, 'facturas/factura_lista.html', {'clientes': clientes})

def factura_remove(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('factura_lista')
