from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Post, PostLike
from .serializers import PostLikeSerializer

class PostLikeToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        value = request.data.get('value')
        if value not in ['like', 'dislike']:
            return Response({'detail': 'Value must be "like" or "dislike".'}, status=status.HTTP_400_BAD_REQUEST)

        obj, created = PostLike.objects.update_or_create(
            post=post,
            user=request.user,
            defaults={'value': value}
        )

        serializer = PostLikeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
