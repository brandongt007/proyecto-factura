from django.contrib import admin
from facturas.models import Cliente, ClienteAdmin, Producto, ProductoAdmin

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
