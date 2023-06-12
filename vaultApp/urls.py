from django.urls import path

from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    path("login/", views.login_view, name="login"),
]
