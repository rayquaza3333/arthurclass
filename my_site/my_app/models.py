
from django.db import models
from django.utils import timezone

# Create your models here.
class Homework(models.Model):
    """Model definition for Homework."""
    lecture = models.CharField( max_length=50)    
    questions = models.TextField(null = True)
    question_img = models.ImageField( upload_to='homeworks', null='True')
    answers = []

    def __str__(self):
        return self.lecture 

    def add_question(self, index, question):
        questions.append(question)
        self.save()
    
    def add_answer(self, index, answer):
        answers.append(answer)
        self.save()
    
    def remove_question(self, index):
        questions.pop(index)
        self.save()
    
    def remove_answer(self, index):
        answers.pop(index)
        self.save()