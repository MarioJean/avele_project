from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    inquiry = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Contact from {}'.format(self.name)
