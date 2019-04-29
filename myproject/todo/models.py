from django.db import models
import datetime
from django.utils import timezone

def now_plus_10():
    return datetime.datetime.now() + datetime.timedelta(days = 10)

class Task(models.Model):
    STATUS_CHOICES = (
                   ('in_progress', 'In progress'),
                   ('completed', 'Completed'),
                   ('pending', 'Pending'),
                   )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    date_time = models.DateTimeField(default=now_plus_10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                          choices=STATUS_CHOICES,
                          default='draft')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
