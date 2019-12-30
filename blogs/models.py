from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=350)
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.author.username}-{self.title}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
