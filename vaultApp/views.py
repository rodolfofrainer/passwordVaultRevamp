from django.shortcuts import render


def index_view(request):
    return render(request, 'vaultApp/index.html')


def login_view(request):
    return render(request, 'vaultApp/login.html')


def about_view(request):
    return render(request, 'vaultApp/about.html')
