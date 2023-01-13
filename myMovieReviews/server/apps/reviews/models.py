from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=24, default="")
    director = models.CharField(max_length=24, default="")
    actor = models.CharField(max_length=24, default="")
    genre = models.CharField(max_length=12, default="")
    stars = models.FloatField(default=0)
    createDate = models.CharField(max_length=12, default="")
    runtime = models.IntegerField(default=0)
    content = models.TextField(default="")