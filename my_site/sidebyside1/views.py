from django.shortcuts import render
from .models import Recording
from django.views.generic import ListView, TemplateView, DetailView, CreateView

# Create your views here.


class RecordingListView(ListView):
    model = Recording
