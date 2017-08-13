from django.db import models

# Create your models here.


class frameInfo(models.Model):
    sname = models.CharField(max_length=32, default=None)
    name = models.CharField(max_length=32)
    fork_num = models.IntegerField()
    star_num = models.IntegerField()
    watch_num = models.IntegerField()
    http_link = models.URLField()
    img_link = models.URLField()
    description = models.TextField()
