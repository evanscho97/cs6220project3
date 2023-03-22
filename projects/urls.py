from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("cart/", views.project_shopping_cart, name="project_shopping_cart"),
    path("<int:pk>/remove/", views.project_remove, name="project_remove"),
    path("<int:pk>/add/", views.project_add, name="project_add"),
]