from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Category, Post
from .serializers import CategorySerializer, CategoryPostSerializer
from .permissions import IsAdminOrReadOnly

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

class CategoryPostListView(generics.ListAPIView):
    serializer_class = CategoryPostSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(category__slug=slug, status='published')
