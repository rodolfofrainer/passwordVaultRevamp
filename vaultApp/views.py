from django.shortcuts import render
from .forms import VaultItemForm
from .models import VaultItemModel


def index_view(request):
    if request.user.is_authenticated:
        context = {
                    'user': request.user,
                    'items': VaultItemModel.objects.filter(vault_item_user_id=request.user.id)
                    }
        return render(request, 'vaultApp/index_loggedin.html', context)
    return render(request, 'vaultApp/index.html')

def about_view(request):
    return render(request, 'vaultApp/about.html')


def vault_item_create_view(request):
    form = VaultItemForm(request.POST or None)
    if form.is_valid():
        vault_item = form.save(commit=False)
        vault_item.vault_item_user_id = request.user.id
        vault_item.save()
        form = VaultItemForm()
    context = {'form': form}
    return render(request, 'vaultApp/vault_item_create.html', context)
