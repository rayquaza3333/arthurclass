from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Homework

# Code start here


class HomePage(TemplateView):
    template_name = "index.html"
    model = Homework