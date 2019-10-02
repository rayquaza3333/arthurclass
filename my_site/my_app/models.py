
from django.db import models
from django.utils import timezone

# Create your models here.


class Lecture(models.Model):
    """
    This model is to store lecture key notes  for student"""
    tutor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateField(auto_now=True, auto_now_add=False)   
    published_date = models.DateField(auto_now=False, auto_now_add=False)
    published = models.BooleanField(default=False)

    def publish(self):
        published = True
        published_date = timezone.now()

    def __str__(self):
        return self.title


class Homework(models.Model):
    """Model definition for Homework."""
    lecture = models.ForeignKey('my_app.Lecture', related_name='homeworks',
                                on_delete=models.CASCADE)
    questions = []

    def __str__(self):
        return self.title + ' ' + student.username + 'homework'

    def add_question(self, index, question):
        questions.append(question)
        self.save()
    def remove_question(self, index):
        questions.pop(index)
        self.save()
    

class Answer(models.Model):
    """Model definition for Answer."""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    homework = models.ForeignKey('my_app.Homework', on_delete=models.CASCADE)
    answers = []

    def add_answer(self, index, answer):
        answers.append(answer)
        self.save()

    def remove_answer(self, index):
        answers.pop(index)
        self.save()

