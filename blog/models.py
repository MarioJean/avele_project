from django.db import models
from datetime import datetime

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[('health', 'health'), ('fitness', 'fitness'),
                                ('lifestyle', 'lifestyle'), ('workout', 'workout')])
    article = models.TextField()
    highlight_text = models.TextField(default="Keep Moving Forward")
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    read_time = models.CharField(max_length=10, default="5 min")
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['publish']

    def __str__(self):
        return 'Comment by {}'.format(self.name)
    

