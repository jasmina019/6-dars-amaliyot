from django.urls import path
from .views.like_views import PostLikeToggleView

urlpatterns = [
    path('posts/<slug:slug>/like/', PostLikeToggleView.as_view(), name='post-like'),
]
