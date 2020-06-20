import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BooleanField
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Local, Password


def index(request):
    locations = Local.objects.filter(verified=True).order_by('name').all()
    return render(request, "index.html", {"locations": locations})


class CreateLocal(LoginRequiredMixin, CreateView):
    model = Local
    fields = ('name', 'location')
    template_name = "create_local.html"
    success_url = "/"

    def form_valid(self, form):
        response = super(CreateLocal, self).form_valid(form)
        if self.request.user.is_staff:
            self.object.verified = True
        else:
            self.object.verified = False
        self.object.save()
        return response


class CreatePassword(LoginRequiredMixin, CreateView):
    model = Password
    fields = ('value', 'location')
    template_name = "create_password.html"
    success_url = "/"

    def form_valid(self, form):
        response = super(CreatePassword, self).form_valid(form)
        if self.request.user.is_staff:
            self.object.verified = True
        else:
            self.object.verified = False
        self.object.save()
        return response


def about(request):
    return render(request, "about.html")


def verify_local(request):
    if request.user.is_staff:
        all_unverified_locals = Local.objects.filter(verified=False).all()
        return render(request, "verify_locals.html", {"locals": all_unverified_locals})
    return redirect("/accounts/login/")


def verify_this_local(request, pk):
    local = Local.objects.get(id=pk)
    local.verified = True
    local.save()
    return redirect("/verify_local/")


def rest_locals(request):
    ls = Local.objects.all()
    to_dump = []
    for local in ls:
        l = {
            "name": local.name,
            "address": local.location,
            "password": local.get_password(),
            "verified": local.verified
        }
        to_dump.append(l)
    data = json.dumps(to_dump)
    return HttpResponse(data, content_type='application/json')
