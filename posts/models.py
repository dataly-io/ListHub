# posts/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DatTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
