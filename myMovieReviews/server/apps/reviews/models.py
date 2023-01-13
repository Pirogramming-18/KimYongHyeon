from django.db import models

# Create your models here.
class Review(models.Model):
    src = models.CharField(max_length=100, default="https://picsum.photos/300/400")
    title = models.CharField(max_length=24, default="")
    director = models.CharField(max_length=24, default="")
    actor = models.CharField(max_length=24, default="")
    genre = models.CharField(max_length=12, default="")
    stars = models.FloatField(default=0)
    createDate = models.DateField(max_length=12, default="")
    runtime = models.IntegerField(default=0)
    explain = models.CharField(max_length=200, default="대통령은 국무회의의 의장이 되고, 국무총리는 부의장이 된다. 국회는 국민의 보통·평등·직접·비밀선거에 의하여 선출된 국회의원으로 구성한다. 헌법개정은 국회재적의원 과반수 또는 대통령의 발의로 제안된다.")
    content = models.TextField(default="")