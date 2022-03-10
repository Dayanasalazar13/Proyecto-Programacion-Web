import email
from pyexpat import model
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UsuariosTabla




class UserRegisterForm(forms.ModelForm):
    class Meta:
      model = UsuariosTabla

      fields = [ 
          'username', 
          'nombre',
          'apellido',
          'email', 
          'password1', 
          'password2',
      ] 

  
      widgets ={
          'username':forms.TextInput(attrs={'class':'form-control','required':''}),
          'apellido':forms.TextInput(attrs={'class':'form-control','required':''}),
          'nombre':forms.TextInput(attrs={'class':'form-control','required':''}),
          'correo':forms.EmailInput(attrs={'class':'form-control','required':''}),
          'password1':forms.PasswordInput(attrs={'class':'form-control','required':''}),
          'password2':forms.PasswordInput(attrs={'class':'form-control','required':''}),
          
      }
    