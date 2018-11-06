from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^factura/nueva/$', views.factura_nueva, name='factura_nueva'),
    ]
