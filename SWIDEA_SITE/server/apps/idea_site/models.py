from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tool(models.Model):
    name = models.CharField(max_length=50, default='')
    kind = models.CharField(max_length=50, default='')
    content = models.TextField(default='')

class Idea(models.Model):
    title = models.CharField(max_length=50, default='')
    image = models.ImageField(blank=True, upload_to='idea_site/%Y%m%d', null=True)
    content = models.TextField()
    interest = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    devtool = models.ForeignKey(Tool, on_delete=models.PROTECT, related_name='Tool', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    idea_star = models.BooleanField(default=False)


