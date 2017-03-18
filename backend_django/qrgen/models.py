from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uid = models.CharField(max_length=32)
    ts = models.DateTimeField()
    pub_key = models.BinaryField()

    def __str__(self):
        return self.uid + ":" + self.pub_key
