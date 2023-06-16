from django.shortcuts import render
from .forms import VaultItemForm


def index_view(request):
    if request.user.is_authenticated:
        return render(request, 'vaultApp/index_loggedin.html', {'user': request.user})
    return render(request, 'vaultApp/index.html')

def about_view(request):
    return render(request, 'vaultApp/about.html')


def vault_item_create_view(request):
    form = VaultItemForm(request.POST or None)
    if form.is_valid():
        vault_item=form.save(commit=False)
        vault_item.user = request.user
        form.save()
        form = VaultItemForm()
    context = { 'form': form }
    return render(request, 'vaultApp/vault_item_create.html', context)