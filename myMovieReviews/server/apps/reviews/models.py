from django.db import models

# Create your models here.
class Reviews(models.Model):
    title = models.CharField(max_length=24)
    director = models.CharField(max_length=24)
    actor = models.CharField(max_length=24)
    genre = models.CharField(max_length=12)
    stars = models.FloatField(default=0)
    runtime = models.models.IntegerField(default=0)
    content = models.TextField()