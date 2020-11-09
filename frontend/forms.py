from django import forms
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_time', 'read_status']
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

        def clean(self):
            pass


class MembershipForm(ModelForm):
    class Meta:
        model = Register
        exclude = ['date_time', 'membership_status']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Name'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Residential Address'}),
            'district': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'District'}),
            'state': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Country'}),
            'pin': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'PIN'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Phone Number'}),
            'age': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Age'}),
        }

        def clean(self):
            pass
