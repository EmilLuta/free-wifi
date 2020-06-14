from django.contrib import admin

# Register your models here.
from .models import Local, Password

admin.site.register(Local)
admin.site.register(Password)
