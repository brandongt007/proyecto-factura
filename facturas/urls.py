from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^factura/nueva/$', views.factura_nueva, name='factura_nueva'),
    path('', views.factura_lista, name='factura_lista'),
    path('factura/lista', views.factura_lista, name='factura_lista'),
    url(r'^factura/(?P<pk>\d+)/remove/$', views.factura_remove, name='factura_remove'),
    ]
