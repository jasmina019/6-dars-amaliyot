from .models import PostLike

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user', 'value', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
