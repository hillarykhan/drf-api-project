from typing import Match
from django.db import models

from drf_api.drf_api.settings import AUTH_PASSWORD_VALIDATORS

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        
