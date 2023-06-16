from django import forms

from .models import VaultItemModel

class VaultItemForm(forms.ModelForm):
    class Meta:
        model = VaultItemModel
        fields = ["vault_item_website", "vault_item_username", "vault_item_password"]