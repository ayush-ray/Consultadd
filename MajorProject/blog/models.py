from django.db import models

class Blog(models.Model):
    bid = models.CharField(max_length=20)
    bname = models.CharField(max_length=100)
    bcontent = models.CharField(max_length=1000)
    class Meta:
        db_table = "blog"