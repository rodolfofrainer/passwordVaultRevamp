from django.shortcuts import render, get_object_or_404, redirect
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

def vault_item_delete_view(request, vault_item_id):
    vault_item = get_object_or_404(VaultItemModel, pk=vault_item_id)
    print(request.user == vault_item.vault_item_user)

    if request.user == vault_item.vault_item_user:
        if request.method == 'POST':
            vault_item.delete()
            return redirect('index')
        else:
            return render(request, 'vaultApp/vault_item_delete.html', {'vault_item': vault_item})
    else:
        return render(request, 'vaultApp/vault_item_delete.html', {'error_message': 'You do not have permission to delete this item.'})