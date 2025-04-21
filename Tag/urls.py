from django.urls import path
from .views.tag_views import (
    TagListCreateView,
    TagDetailView,
    TagPostListView
)

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<slug:slug>/', TagDetailView.as_view(), name='tag-detail'),
    path('tags/<slug:slug>/posts/', TagPostListView.as_view(), name='tag-posts'),
]
