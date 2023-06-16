from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets


class VaultUserModel(AbstractUser):
    # Add any additional fields or customizations you need

    class Meta:
        verbose_name_plural = "VaultUserModels"

    def __str__(self):
        return self.username


random_salt = secrets.token_hex(32)


class VaultItemModel(models.Model):
    user = models.ForeignKey(VaultUserModel, on_delete=models.CASCADE, related_name='vault_items')
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=255, default=random_salt)

    def __str__(self):
        return str(self.website)


class PepperModel(models.Model):
    user = models.OneToOneField(VaultUserModel, on_delete=models.CASCADE, related_name='pepper')
    pepper = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)
