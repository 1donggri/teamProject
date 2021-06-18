from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=False, blank=False, null=False)

    def __str__(self):
        return "%s - %s" % (self.username, self.title)

