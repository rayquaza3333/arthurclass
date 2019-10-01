from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                ListView, DeleteView, FormView,
                                CreateView)
from .models import Homework, Answer

# Code start here


# Home Page
class HomePage(TemplateView):
    template_name = "index.html"
    model = Homework


# Classes for Homework
class HomeworkListView(ListView):
    model = Homework


class HomeworkCreateView(CreateView):
    model = Homework
    template_name = "TEMPLATE_NAME"


class HomeworkDeleteView(DeleteView):
    model = Homework
    template_name = "TEMPLATE_NAME"


class HomeworkUpdateView(UpdateView):
    model = Homework
    template_name = "TEMPLATE_NAME"


# Classes for answer 

class AnswerListView(ListView):
    model = Answer


class AnswerCreateView(CreateView):
    model = Answer
    template_name = "TEMPLATE_NAME"


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = "TEMPLATE_NAME"


class AnswerUpdateView(UpdateView):
    model = Answer
    template_name = "TEMPLATE_NAME"

