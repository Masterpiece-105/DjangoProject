from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.ImageField(upload_to="posts/", default='')
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.title} - {self.content} - {self.image}"
    
    