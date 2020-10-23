from django import forms
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_time']
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

        def clean(self):
            pass


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

        def clean(self):
            pass
