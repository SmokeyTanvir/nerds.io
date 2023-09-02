from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("delete/<str:title>", views.delete, name="delete_entry"),
    path("random-page", views.random, name="random_page"),
    path("wiki/<str:title>", views.entry, name="entry"),
]