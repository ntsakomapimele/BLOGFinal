from django.contrib import admin
from blog_app.models import Topic, Post, Comment

# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)