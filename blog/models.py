from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.ImageField(upload_to="posts/", default='')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title} - {self.content} - {self.image}"
    
class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.user.username} on {self.post.title}"