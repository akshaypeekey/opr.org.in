from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *



class Home(TemplateView):
    model = Index
    template_name = "dashboard.html"
    form_class = IndexForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


class About(TemplateView):
    model = About
    template_name = "about.html"
    form_class = AboutForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


class Vision(TemplateView):
    model = Vision
    template_name = "vision.html"
    form_class = VisionForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


class Events(TemplateView):
    model = Events
    template_name = "events.html"
    form_class = EventsForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


class Contact(TemplateView):
    model = Contact
    template_name = "contact.html"
    form_class = ContactForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)

