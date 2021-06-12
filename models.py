from django.db import models
from django.contrib.auth.models import User


class Todouser(models.Model):
    user_todo = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=25,null=False)
    description=models.CharField(max_length=100,null=False)
