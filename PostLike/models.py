from django.db import models
from django.contrib.auth.models import User

class PostLike(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    VALUE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=VALUE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # har bir user faqat bir marta like/dislike qilsin

    def __str__(self):
        return f'{self.user.username} - {self.post.title} - {self.value}'
