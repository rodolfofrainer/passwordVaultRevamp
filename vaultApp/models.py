from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets


class VaultUserModel(AbstractUser):
    # Add any additional fields or customizations you need

    class Meta:
        verbose_name_plural = "Vault User Models"

    def __str__(self):
        return str(self.username)


random_salt = secrets.token_hex(32)


class VaultItemModel(models.Model):
    vault_item_user = models.ForeignKey(VaultUserModel, on_delete=models.CASCADE, related_name='vault_items')
    vault_item_website = models.CharField(max_length=100)
    vault_item_username = models.CharField(max_length=100)
    vault_item_password = models.CharField(max_length=100)
    vault_item_salt = models.CharField(max_length=255, default=random_salt)

    def __str__(self):
        return str(self.vault_item_website)


class PepperModel(models.Model):
    pepper_user = models.OneToOneField(VaultUserModel, on_delete=models.CASCADE, related_name='pepper')
    pepper = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pepper_user)
