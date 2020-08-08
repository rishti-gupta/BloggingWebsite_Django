from django.db import models
import uuid


class Blog(models.Model):
    uname = models.CharField(max_length=100, default="")
    bid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    bname = models.CharField(max_length=100, default="")
    bcontent = models.CharField(max_length=1000, default="")
    class Meta:
        db_table = "blog"
