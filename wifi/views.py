from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Local, Password


def index(request):
    locations = Local.objects.order_by('name').all()
    return render(request, "index.html", {"locations": locations})


class CreateLocal(CreateView, LoginRequiredMixin):
    model = Local
    fields = ('name', 'location')
    template_name = "create_local.html"
    success_url = "/"


class CreatePassword(CreateView, LoginRequiredMixin):
    model = Password
    fields = ('value', 'location')
    template_name = "create_password.html"
    success_url = "/"


def about(request):
    return render(request, "about.html")
