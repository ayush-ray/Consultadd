from django.db import models
# from hashid_field import HashidAutoField

class Blog(models.Model):
    uname = models.CharField(max_length=100, default="")
#     bid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     bid = HashidAutoField(primary_key=True)
    bname = models.CharField(max_length=100, default="")
    bcontent = models.CharField(max_length=1000, default="")
    class Meta:
        db_table = "blog"
