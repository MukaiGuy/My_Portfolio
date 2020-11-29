# from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


# For later use
'''
class Repo(models.Model):
    genre = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstact = models.CharField(max_length=255)
    #link = models.urlField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    pass
'''