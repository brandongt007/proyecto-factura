from django import forms
from .models import Producto, Cliente

class ClienteForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Cliente
        fields = ('nit', 'nombre', 'apellido', 'direccion', 'email', 'telefono', 'productos')

def __init__ (self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields["productos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["productos"].help_text = "Ingrese Productos"
        self.fields["productos"].queryset = Producto.objects.all()

class ProductoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'stock')
