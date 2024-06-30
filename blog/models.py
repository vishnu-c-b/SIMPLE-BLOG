from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    content = models.TextField()
    publication_date = models.DateField(default=timezone.now, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)

    def __str__(self):
        return self.title