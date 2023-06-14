from django.shortcuts import render


def index_view(request):
    if request.user.is_authenticated:
        return render(request, 'vaultApp/index_loggedin.html', {'user': request.user})
    return render(request, 'vaultApp/index.html')


def about_view(request):
    return render(request, 'vaultApp/about.html')
