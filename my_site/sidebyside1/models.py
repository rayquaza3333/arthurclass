from django.db import models

# Create your models here.


class Recording(models.Model):
    """Model definition for Homework."""

    title = models.CharField(max_length=256, default='Not uploaded')
    recording = models.FileField(upload_to='sidebyside1')

    def __str__(self):
        return self.title
