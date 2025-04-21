from django.urls import path
from .views.category_views import (
    CategoryListCreateView,
    CategoryDetailView,
    CategoryPostListView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<slug:slug>/posts/', CategoryPostListView.as_view(), name='category-posts'),
]
