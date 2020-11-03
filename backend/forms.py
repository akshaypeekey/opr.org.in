from django import forms
from django.forms import ModelForm
from backend.models import *


class IndexForm(ModelForm):
    class Meta:
        model = Index
        exclude = ['index_title']
        widgets = {
            'index_about_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'index_about_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'index_about_three': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'index_about_four': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'index_mission_one': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_two': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_three': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_four': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_five': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_six': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_seven': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_eight': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_nine': forms.TextInput(attrs={'class': 'form-control'}),
            'index_mission_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'index_event_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'index_event_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'index_event_three': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

        def clean(self):
            pass


class AboutForm(ModelForm):
    class Meta:
        model = AboutUS
        exclude = ['about_title']
        widgets = {
            'about_us_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'about_us_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'about_number_one': forms.TextInput(attrs={'class': 'form-control'}),
            'about_number_two': forms.TextInput(attrs={'class': 'form-control'}),
            'about_number_three': forms.TextInput(attrs={'class': 'form-control'}),
            'about_number_four': forms.TextInput(attrs={'class': 'form-control'}),
            'about_sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_sub_para': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'about_sub_para_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
            'about_sub_para_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
            'about_sub_para_three': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
        }

        def clean(self):
            print("inside clean")


class VisionForm(ModelForm):
    class Meta:
        model = VisionMission
        exclude = ['vision_title']
        widgets = {
            'vision_para_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'vision_para_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'mission_para_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'mission_para_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'mission_para_three': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'mission_para_four': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'download_cp':forms.FileInput(),
            'download_copr': forms.FileInput(),
            'manifesto_language': forms.TextInput(attrs={'class': 'form-control'}),
            'download_manifesto': forms.FileInput(),
        }

        def clean(self):
            pass


class EventsForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['events_title']
        widgets = {
            'events_para_one': forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}),
            'events_para_two': forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}),
            'events_para_three': forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}),
            'events_para_four': forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}),
        }


        def clean(self):
            pass