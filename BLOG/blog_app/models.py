from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Topic(models.Model):
    topic_name = models.CharField(max_length= 256)
    
    def __str__(self):
        return self.topic_name
    
    
class Post(models.Model):
    title = models.CharField(max_length=264)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='articles')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


