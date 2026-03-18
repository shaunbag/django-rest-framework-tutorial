from django.urls import  path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import api_root, SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter 

""" 
class based views 
"""
# urlpatterns = [
#     path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
#     path("snippets/<int:pk>", views.SnippetDetail.as_view(), name="snippet-detail"),
#     path("users/", views.UserList.as_view(), name="user-list"),
#     path("users/<int:pk>", views.UserDetail.as_view(), name="user-detail"),
#     path("api-auth/", include("rest_framework.urls")),
#     path("", views.api_root),
#     path("snippets/<int:pk>/highlight", views.SnippetHighlight.as_view(), name="snippet-highlight")
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


"""
    Viewset based urls with the URL configuration designs
"""
snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view({
    "get": "retrive", "put": "update", "patch": "partial_update", "delete": "destroy"
})
snippet_highlight = SnippetViewSet.as_view({
    "get": "highlight"
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})


urlpatterns = format_suffix_patterns([
    path("", api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
    path("users/", user_list, name="user-list"),
    path("user/<int:pk>/", user_detail, name="user-detail")
])

"""
    Viewset based urls using routers
"""
# router = DefaultRouter()
# router.register(r"snippets", views.SnippetViewSet, basename="snippet")
# router.register(r"users", views.UserViewSet, basename="users")

# urlpatterns = [
#     path("", include(router.urls))
# ]
