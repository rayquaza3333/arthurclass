from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=256)
    text = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    