from django.shortcuts import render
from django.views.generic import CreateView

from .models import Local, Password


def index(request):
    locations = Local.objects.order_by('name').all()
    return render(request, "index.html", {"locations": locations})


class CreateLocal(CreateView):
    model = Local
    fields = ('name', 'location')
    template_name = "create_local.html"
    success_url = "/"


class CreatePassword(CreateView):
    model = Password
    fields = ('value', 'location')
    template_name = "create_password.html"
    success_url = "/"


def about(request):
    return render(request, "about.html")
