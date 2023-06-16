from django import forms

from .models import VaultItemModel

class VaultItemForm(forms.ModelForm):
    class Meta:
        model = VaultItemModel
        fields = ["website", "username", "password"]