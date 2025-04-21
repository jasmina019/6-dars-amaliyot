from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Tag, Post
from .serializers import TagSerializer, TagPostSerializer
from .permissions import IsAdminOrReadOnly

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

class TagPostListView(generics.ListAPIView):
    serializer_class = TagPostSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(tags__slug=slug, status='published')
