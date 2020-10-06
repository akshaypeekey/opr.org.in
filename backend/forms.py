from django.forms import ModelForm
from backend.models import *


class IndexForm(ModelForm):
    class Meta:
        model = Index
        fields = "__all__"

        def clean(self):
            pass


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = "__all__"

        def clean(self):
            pass


class VisionForm(ModelForm):
    class Meta:
        model = Vision
        fields = "__all__"

        def clean(self):
            pass


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"

        def clean(self):
            pass


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        def clean(self):
            pass


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

        def clean(self):
            pass
