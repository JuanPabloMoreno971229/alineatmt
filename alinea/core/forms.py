from tkinter import Label
from django import forms
from django.forms import widgets 
from .models import Contact


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':' col-lg-12 d-flex flex-column','placeholder':'Nombre'}),
            'mail' : forms.EmailInput(attrs={'class':' col-lg-12 d-flex flex-column','placeholder':'Correo'}),
            'phone' : forms.TextInput(attrs={'class':' col-lg-12 d-flex flex-column','placeholder':'Teléfono'}),
            'message' : forms.TextInput(attrs={'class':' col-lg-12 d-flex flex-column','placeholder':'Mensaje'}),
            'status' : forms.HiddenInput(attrs={'class':' col-lg-12 d-flex flex-column','placeholder':'Estado'}),
        }
        labels = {'name': '', 'mail': '', 'phone': '', 'message': ''}
    
    
    

