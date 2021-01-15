from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0, 'Draft'), 
    (1, 'Publish')
)


class Category(models.Model):
    """
    Categories for posts
    """
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=timezone.now().strftime('%Y-%m-%d'))
    updated = models.DateField(auto_now=timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
