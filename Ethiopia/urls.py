from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("graphs/<str:id>", views.graphs, name="graphs"),
    path("elements", views.elements, name="elements")
]