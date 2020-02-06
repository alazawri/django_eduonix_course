from django.db import models
from django.contrib.auth.models import User


class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    blog_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'title: {self.title}'