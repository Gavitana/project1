from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/edit/<title>", views.edit , name = "edit"),
    path("random/", views.random_page, name="random"),
    path("wiki/<title>", views.page, name="page"),
    path("add",views.add, name = "add"),
    path("search", views.search , name = "search")
]
