from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username


class Books(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    synopsis = models.TextField()
    review = models.TextField()
    feature = models.BooleanField(default=False)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
