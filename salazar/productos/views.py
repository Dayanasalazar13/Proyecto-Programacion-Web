from webbrowser import get
from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import context, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import UsuariosTabla
from.forms import UserRegisterForm

# Create your views here.
def home(request):
    template =loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('productos/index.html')
    context ={}
    return HttpResponse(template.render(context, request))

def catalogo(request):
    template = loader.get_template('productos/catalogo.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
def new_usuario(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, "Te has registrado correctamente")
            return HttpResponseRedirect(reverse('catalogo'))
    else: 
        form = UserRegisterForm()  
        
    return render(request, 'productos/crear_usuario.html',{'form':form} )

def consultaUser(request):
    usuarios=UsuariosTabla.objects.all()
    template =loader.get_template('productos/consultaUser.html')
    context={
        "usuarios":usuarios
    }
    return HttpResponse(template.render(context,request))


def baby(request):
    template =loader.get_template('productos/baby.html')
    context = {}
    return HttpResponse(template.render(context,request))

def hombre(request):
    template =loader.get_template('productos/hombre.html')
    context = {}
    return HttpResponse(template.render(context,request))

def masha(request):
    template =loader.get_template('productos/masha.html')
    context = {}
    return HttpResponse(template.render(context,request))

def matrimonio(request):
    template =loader.get_template('productos/matrimonio.html')
    context = {}
    return HttpResponse(template.render(context,request))

def minnie(request):
    template =loader.get_template('productos/minnie.html')
    context = {}
    return HttpResponse(template.render(context,request))

def mujer(request):
    template =loader.get_template('productos/mujer.html')
    context = {}
    return HttpResponse(template.render(context,request))

def quince(request):
    template =loader.get_template('productos/quince.html')
    context = {}
    return HttpResponse(template.render(context,request))

def unicornio(request):
    template =loader.get_template('productos/unicornio.html')
    context = {}
    return HttpResponse(template.render(context,request))

def hombre3(request):
    template =loader.get_template('productos/hombre3.html')
    context = {}
    return HttpResponse(template.render(context,request))

def quinces(request):
    template =loader.get_template('productos/quinces.html')
    context = {}
    return HttpResponse(template.render(context,request))


