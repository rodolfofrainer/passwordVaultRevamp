from django.contrib import admin
from .models import VaultUserModel, VaultItemModel, Salt

# Register your models here.

admin.site.register(VaultUserModel)
admin.site.register(VaultItemModel)
admin.site.register(Salt)