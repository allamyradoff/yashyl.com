from django import forms
from .models import *
from django.forms.widgets import Select


class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ady',
        'class': 'form-control',
        'style':"margin-top:5%"
    }))

    desc = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Beýany',
        'class': 'form-control',
        'style':"margin-top:2%"
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Bahasy TMT',
        'class': 'form-control',
        'style':"margin-top:2%"
    }))
    sale_percent = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Skidka процент',
        'class': 'form-control',
        'style':"margin-top:2%"
    }))

    sale_price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Skidkadaky bahasy',
        'class': 'form-control',
        'style':"margin-top:2%"
    }))


    # image = forms.FileField(widget=forms.FileInput(attrs={
    # }))

    # image_1 = forms.FileField(required=False, widget=forms.FileInput(attrs={
    # }))

    # image_2 = forms.FileField(required=False, widget=forms.FileInput(attrs={
    # }))


    class Meta:
        model = StoreProduct
        fields = ('name', 'desc', 'price', 'store', 'image', 'image_1',
                  'image_2',  'sale_percent', 'sale_price')
        # widgets = {
        #     'store': Select(attrs={'class': 'form-control', }),
        # }
        required = (
            'store',
        )
