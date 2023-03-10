from django import forms
from .models import *
from django.forms.widgets import Select


class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ady',
        'class': 'form-control',
    }))

    desc = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Beýany',
        'class': 'form-control',
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Bahasy TMT',
        'class': 'form-control',
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
                  'image_2',  'sale_percent', 'sale_price', 'stock')
        # widgets = {
        #     'store': Select(attrs={'class': 'form-control', }),
        # }
        required = (
            'store',
        )
