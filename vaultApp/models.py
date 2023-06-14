from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VaultUserModel(models.Model):
    username = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username


class VaultItemModel(models.Model):
    user = models.ForeignKey(VaultUserModel, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.website

class Salt(models.Model):
    user = models.ForeignKey(VaultUserModel, on_delete=models.CASCADE)
    salt = models.CharField(max_length=100)
    def __str__(self):
        return self.salt