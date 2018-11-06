from django.shortcuts import render
from django.contrib import messages
from .forms import ProductoForm
from facturas.models import Producto, Factura

def factura_nueva(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            producto = Producto.objects.create(nombre=formulario.cleaned_data['nombre'], precio = formulario.cleaned_data['precio'], stock = formulario.cleaned_data['stock'])
            for cliente_id in request.POST.getlist('clientes'):
                factura = Factura(cliente_id=cliente_id, producto_id = producto.id)
                factura.save()
            messages.add_message(request, messages.SUCCESS, 'Producto Guardada Exitosamente.')
    else:
        formulario = ProductoForm()
    return render(request, 'facturas/factura_editar.html', {'formulario': formulario})
