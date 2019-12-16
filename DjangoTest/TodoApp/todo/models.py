from django.db import models

# Create your models here.
from django.utils import timezone


class Todo(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.content


