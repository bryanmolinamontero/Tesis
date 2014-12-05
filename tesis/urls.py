from django.conf.urls import patterns, include, url

from cerraduras.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tesis.views.home', name='home'),
    # url(r'^tesis/', include('tesis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index/$', index),

    url(r'^login/$', login),
    url(r'^verificar/$', verificarLogin),
    url(r'^cerrarSesion/$', cerrarSesion),


    url(r'^lab1/$', lab1),
    url(r'^lab2/$', lab2),
    url(r'^lab3/$', lab3),
    url(r'^lab4/$', lab4),
    url(r'^lab5/$', lab5),
    url(r'^lab6/$', lab6),




    url(r'^administrador/$', administrador),
    url(r'^usuario/$', usuario),
    url(r'^usuarioEspecifico/$', usuarioEspecifico),

    #usuarios
    url(r'^nuevoUsuario/$', nuevoUsuario),
    url(r'^ingresarUsuario/$', ingresarUsuario),
    url(r'^editarUsuario/$', editarUsuario),
    url(r'^eliminarUsuario/$', eliminarUsuario),
    url(r'^comprobarUsername/$', comprobarUsername),
    url(r'^comprobarPasswords/$', comprobarPasswords),
)
