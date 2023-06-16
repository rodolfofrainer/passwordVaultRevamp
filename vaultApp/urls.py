from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("about/", views.about_view, name="about"),
    path("vault/create_new_item", views.vault_item_create_view, name="create_new_item"),
]

