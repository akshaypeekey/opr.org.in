from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from .forms import *
from .models import *


class Home(TemplateView):
    model = Index
    template_name = "dashboard.html"
    form_class = IndexForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)


class IndexUpdateView(SuccessMessageMixin, UpdateView):
    model = Index
    form_class = IndexForm
    template_name = 'index.html'
    success_message = 'Data Updated Successfully!!!!'

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class AboutUpdateView(SuccessMessageMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'about.html'
    success_message = 'Data Updated Successfully!!!!'

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class VisionUpdateView(SuccessMessageMixin, UpdateView):
    model = Vision
    form_class = VisionForm
    template_name = 'vision.html'
    success_message = 'Data Updated Successfully!!!!'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class EventsUpdateView(SuccessMessageMixin, UpdateView):
    model = Events
    form_class = EventsForm
    template_name = 'events.html'
    success_message = 'Data Updated Successfully!!!!'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class Contact(TemplateView):
    model = Contact
    template_name = "contact.html"
    form_class = ContactForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


class RegisteredUser(TemplateView):
    model = Contact
    template_name = "registration.html"
    form_class = ContactForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {}
        context['form'] = form
        return render(request, self.template_name, context)

