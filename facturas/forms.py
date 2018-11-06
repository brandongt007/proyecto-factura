from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'stock', 'clientes')

def __init__ (self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields["clientes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["clientes"].help_text = "Ingrese Clientes"
        self.fields["clientes"].queryset = Cliente.objects.all()
