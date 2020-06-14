from django.shortcuts import render

from .models import Local


def index(request):
    locations = Local.objects.order_by('name').all()
    return render(request, "index.html", {"locations": locations})
