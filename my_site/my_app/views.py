from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                ListView, DeleteView, FormView,
                                CreateView, UpdateView)
from .models import Homework

# Code start here


# Home Page
class HomePage(TemplateView):
    template_name = "index.html"
    model = Homework


# Classes for Homework
class HomeworkListView(ListView):
    model = Homework



class HomeworkDetailView(DetailView):
    model = Homework


class HomeworkCreateView(CreateView):
    model = Homework
    fields = ['lecture', 'questions',]


class HomeworkDeleteView(DeleteView):
    model = Homework


class HomeworkUpdateView(UpdateView):
    model = Homework
    fields = '__all__'

# Classes for answer 

# class AnswerListView(ListView):
#     model = Answer


# class AnswerCreateView(CreateView):
#     model = Answer
#     template_name = "TEMPLATE_NAME"


# class AnswerDeleteView(DeleteView):
#     model = Answer
#     template_name = "TEMPLATE_NAME"


# class AnswerUpdateView(UpdateView):
#     model = Answer
#     template_name = "TEMPLATE_NAME"

