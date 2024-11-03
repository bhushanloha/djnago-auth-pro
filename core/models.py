from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Create_User_Profile(models.Model):
    age = models.IntegerField()
    contact = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
