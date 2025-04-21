from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('posts/<slug:slug>/comments/', CommentListCreateView.as_view(), name='post_comments'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment_detail'),
]
