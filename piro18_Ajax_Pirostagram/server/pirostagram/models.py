from django.db import models

class Comment(models.Model):
  comment = models.CharField(max_length=100)
  
class Like(models.Model):
  like = models.BooleanField(default=False)