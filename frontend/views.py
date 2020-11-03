from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from backend.models import *
from backend.forms import *
from .models import *
from .forms import *


class Home(TemplateView):
    model = Index
    template_name = "frontend/index.html"

    def get(self, request, *args, **kwargs):
        data = Index.objects.all()
        context = {'data': data}
        return render(request, self.template_name, context)


class About(TemplateView):
    model = AboutUS
    template_name = "frontend/about.html"

    def get(self, request, *args, **kwargs):
        data = AboutUS.objects.all()
        context = {'data': data}
        return render(request, self.template_name, context)


class Vision(TemplateView):
    model = VisionMission
    template_name = "frontend/vision.html"

    def get(self, request, *args, **kwargs):
        data = VisionMission.objects.all()
        context = {'data': data}
        return render(request, self.template_name, context)


class Events(TemplateView):
    model = Event
    template_name = "frontend/events.html"

    def get(self, request, *args, **kwargs):
        data = Event.objects.all()
        context = {'data': data}
        return render(request, self.template_name, context)


class ContactUS(TemplateView):
    model = Contact
    template_name = "frontend/contact.html"
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)


class Register(TemplateView):
    model = Register
    template_name = "frontend/registration.html"
    form_class = MembershipForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)