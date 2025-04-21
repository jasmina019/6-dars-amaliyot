from django.urls import path
from .views.post_views import (
    PostListCreateView,
    PostDetailView,
    UserPostListView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('users/<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
]
