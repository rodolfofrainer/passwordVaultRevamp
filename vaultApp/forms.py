from django import forms
from django.core.exceptions import ValidationError

from .models import VaultItemModel

class VaultItemForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = VaultItemModel
        fields = ["vault_item_website", "vault_item_username", "vault_item_password", "confirm_password"]
        widgets = {
            "vault_item_password": forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("vault_item_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

