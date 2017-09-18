#from _future_ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    #make sure the list of the title is the title of the created object
    def __str__(self):
        return self.title