from django.db import models
from django.contrib import admin

class Cliente(models.Model):
    nit = models.CharField(max_length=8)
    nombre  =   models.CharField(max_length=50)
    apellido =  models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=8)
    email = models.EmailField()

    def __str__(self):
        return self.nit

class Producto(models.Model):
    nombre    = models.CharField(max_length=60)
    precio    = models.DecimalField(max_digits=5, decimal_places=2)
    stock     = models.IntegerField()
    clientes   = models.ManyToManyField(Cliente, through='Factura')

    def __str__(self):
        return self.nombre

class Factura (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class FacturaInLine(admin.TabularInline):
    model = Factura
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    inlines = (FacturaInLine,)

class ProductoAdmin (admin.ModelAdmin):
    inlines = (FacturaInLine,)
