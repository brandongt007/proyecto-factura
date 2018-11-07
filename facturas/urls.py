from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    path('', views.index, name='index'),
    url(r'^factura/nueva/$', views.factura_nueva, name='factura_nueva'),
    path('factura/lista', views.factura_lista, name='factura_lista'),
    path('factura/<int:pk>/editar/', views.factura_editar, name='factura_editar'),
    url(r'^factura/(?P<pk>\d+)/remove/$', views.factura_remove, name='factura_remove'),
    path('factura/<int:pk>/', views.factura_detalle, name='factura_detalle'),
    path('producto/lista', views.producto_lista, name='producto_lista'),
    url(r'^producto/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
    url(r'^producto/(?P<pk>\d+)/remove/$', views.producto_remove, name='producto_remove'),
    ]
