from django import forms
from .models import *
from django.shortcuts import *

class ProductForm(forms.ModelForm):
    #admin_fk = forms.ModelChoiceField(queryset=Admin.objects.filter(id=request.session['id']))
    class Meta:
        model=Product
        fields= '__all__'
        exclude = ('admin_fk','Date','Image_Name',)