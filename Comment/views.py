from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsCommentAuthorOrPostAuthorOrAdminOrReadOnly

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_slug = self.kwargs['slug']
        return Comment.objects.filter(post__slug=post_slug)

    def perform_create(self, serializer):
        post_slug = self.kwargs['slug']
        from blog.models import Post
        post = Post.objects.get(slug=post_slug)
        serializer.save(author=self.request.user, post=post)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrPostAuthorOrAdminOrReadOnly]
    lookup_field = 'id'
