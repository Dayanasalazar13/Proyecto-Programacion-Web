#from django import template
from django.conf.urls import static
from django.http.response import HttpResponse
from django.template import context
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView 
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns = [...] #aquí irían mis direcciones y al final
#urlpatterns += staticfiles(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns =[
    path('',views.home, name='home'),
    path('consultar-usuarios',views.consultaUser, name='consultaUser'),
    path('productos/', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/new/', views.new_usuario, name='crear_usuarios'),
    path('catalogo/iniciar/', LoginView.as_view(template_name='productos/iniciar_sesion.html'), name='iniciar_sesion'),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    path('catalogo/baby/', views.baby, name='baby'),
    path('catalogo/hombre/', views.hombre, name='hombre'),
    path('catalogo/masha/', views.masha, name='masha'),
    path('catalogo/matrimonio/', views.matrimonio, name='matrimonio'),
    path('catalogo/minnie/', views.minnie, name='minnie'),
    path('catalogo/mujer/', views.mujer, name='mujer'),
    path('catalogo/quince/', views.quince, name='quince'),
    path('catalogo/unicornio/', views.unicornio, name='unicornio'),
    path('catalogo/hombre3/', views.hombre3, name='hombre3'),
    path('catalogo/quinces/', views.quinces, name='quinces'),
]
