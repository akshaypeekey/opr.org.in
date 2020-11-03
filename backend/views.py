from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from .forms import *
from .models import *
from frontend.models import *


class Home(TemplateView):
    model = Index
    template_name = "backend/dashboard.html"
    form_class = IndexForm
    def get(self, request, *args, **kwargs):

        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)


class IndexUpdateView(SuccessMessageMixin, UpdateView):
    model = Index
    form_class = IndexForm
    template_name = 'backend/index.html'
    success_message = 'Data Updated Successfully!!!!'

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class AboutUpdateView(SuccessMessageMixin, UpdateView):
    model = AboutUS
    form_class = AboutForm
    template_name = 'backend/about.html'
    success_message = 'Data Updated Successfully!!!!'

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class VisionUpdateView(SuccessMessageMixin, UpdateView):
    model = VisionMission
    form_class = VisionForm
    template_name = 'backend/vision.html'
    success_message = 'Data Updated Successfully!!!!'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class EventsUpdateView(SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventsForm
    template_name = 'backend/events.html'
    success_message = 'Data Updated Successfully!!!!'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return self.request.path


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "backend/contact.html"


class ContactMessageView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "backend/messages.html"
    context_object_name = "details"


class DeleteMessageView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "backend/message_delete.html"
    context_object_name = "details"
    success_url = reverse_lazy('dashboard')

