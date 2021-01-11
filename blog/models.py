from django.db import models
from datetime import datetime

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[('health', 'health'), ('fitness', 'fitness'),
                                ('lifestyle', 'lifestyle'), ('workout', 'workout')])
    article = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
