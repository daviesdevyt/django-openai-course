from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path("text-generator/", views.textgenView, name="textgen"),
    path("code-generator/", views.codegenView, name="codegen"),
    path("image-generator/", views.imagegenView, name="imagegen"),
    path("gen/<str:model>/", views.gen)
]