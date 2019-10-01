from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                ListView, DeleteView, FormView,
                                CreateView)
from .models import Homework, Lecture

# Code start here


class HomePage(TemplateView):
    template_name = "index.html"
    model = Homework


class LectureListView(ListView):
    model = Lecture


class LectureDetailView(DetailView):
    model = Lecture

class LectureCreateView(CreateView):
    model = Lecture


class LectureDeleteView(DeleteView):
    model = Lecture






class HomeworkListView(ListView):
    model = Homework

clas