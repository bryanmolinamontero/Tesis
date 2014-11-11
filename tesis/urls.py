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


    url(r'^direccion/$', direccion),




    url(r'^administrador/$', administrador),
    url(r'^usuario/$', usuario),

    #usuarios

    url(r'^ingresarUsuario/$', ingresarUsuario),
)
