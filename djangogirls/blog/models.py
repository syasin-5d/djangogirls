from django.db import models
from django.utils import timezone

class post(models.model):
    author = models.foreignkey('auth.user')
    title = models.charfield(max_length=200)
    text = models.textfield()
    created_date = models.datetimefield(default=timezone.now)
    published_date = models.datetimefield(blank=true, null=true)

def publish(self):
    self.published_date = timezone.now
    self.save()

def __str__(self):
    return self.title

