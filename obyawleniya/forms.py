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

    image = forms.FileField(widget=forms.FileInput(attrs={


    }))

    image_2 = forms.FileField(required=False, widget=forms.FileInput(attrs={
    }))

    image_3 = forms.FileField(required=False, widget=forms.FileInput(attrs={


    }))

    locations = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ýerleşýän ýeri',
        'class': 'form-control',
    }))

    class Meta:
        model = Ad
        fields = ('name', 'desc',  'locations', 'phone_number',
                  'image', 'image_2', 'image_3',)
        # widgets = {
        #   'cat_id': Select(attrs={'class': 'form-control',}),
        #   'locations': Select(attrs={'class': 'form-control',}),
        # }


class AdEditForm(forms.ModelForm):

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

    image = forms.FileField(widget=forms.FileInput(attrs={


    }))

    image_2 = forms.FileField(required=False, widget=forms.FileInput(attrs={
    }))

    image_3 = forms.FileField(required=False, widget=forms.FileInput(attrs={


    }))


    locations = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ýerleşýän ýeri',
        'class': 'form-control',
    }))




    


    


    class Meta:
        model = Ad
        fields = ('name', 'desc', 'locations', 'phone_number',  'image', 'image_2', 'image_3',  )
        # widgets = {
        #   'cat_id': Select(attrs={'class': 'form-control',}),
        #   'locations': Select(attrs={'class': 'form-control',}),
        # }