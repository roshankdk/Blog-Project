from importlib import import_module
from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog)