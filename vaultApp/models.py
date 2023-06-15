from django.db import models
from django.contrib.auth.models import User
import secrets


class VaultUserModel(models.Model):
    username = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.username)


random_salt = secrets.token_hex(32)
class VaultItemModel(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(VaultUserModel, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=255, default=random_salt)
    
    def __str__(self):
        return str(self.website)


class PepperModel(models.Model):
    user = models.OneToOneField(VaultUserModel, on_delete=models.CASCADE)
    pepper = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)
