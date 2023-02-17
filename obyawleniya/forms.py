from django import forms
from .models import *
from django.forms.widgets import Select


class AdForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ady',
        'class': 'form-control',
    }))

    desc = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Beýany',
        'class': 'form-control',

    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefon belgiňiz',
        'class': 'form-control',
        'type': "number"

    }))
    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Bahasy TMT',
        'class': 'form-control',

    }))

    exchange = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input required',
        
    }))

    credit = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input required',
        
        
    }))

    image = forms.FileField(widget=forms.FileInput(attrs={

        
    }))

    image_2 = forms.FileField(required=False, widget=forms.FileInput(attrs={
    }))

    image_3 = forms.FileField(required=False, widget=forms.FileInput(attrs={

        
    }))




    


    


    class Meta:
        model = Ad
        fields = ('name', 'desc',  'cat_id', 'locations', 'phone_number', 'exchange',   'credit', 'image', 'image_2', 'image_3', 'price',  )
        widgets = {
          'cat_id': Select(attrs={'class': 'form-control',}),
          'locations': Select(attrs={'class': 'form-control',}),
        }