from django.urls import include, path
from . import views

urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>", views.snippet_detail)
]
